"""REM ERP Backend — Flask app: auth (session + RBAC), REST APIs mirroring the V10 prototype."""
import json, re
from datetime import datetime
from functools import wraps
from flask import Flask, jsonify, request, session
from werkzeug.security import check_password_hash
from db import get_db, rows_to_dicts, row_to_dict, log_activity

app = Flask(__name__)
app.secret_key = 'rem-erp-dev-secret-change-in-prod'

# ── RBAC (mirrors prototype ROLE_MODULES) ─────────────────────────────
ROLE_MODULES = {
    'Super Admin': 'all',
    'Sales Agent': ['leads', 'customers', 'bookings', 'dashboard'],
    'Site Engineer': ['projects', 'assets', 'dashboard'],
    'Finance': ['invoices', 'payments', 'dues', 'customers', 'assets', 'license', 'dashboard'],
}

def require_login(f):
    @wraps(f)
    def wrapper(*a, **kw):
        if 'uid' not in session:
            return jsonify({'error': 'Unauthorized — login required'}), 401
        return f(*a, **kw)
    return wrapper

def require_module(module):
    def deco(f):
        @wraps(f)
        def wrapper(*a, **kw):
            if 'uid' not in session:
                return jsonify({'error': 'Unauthorized'}), 401
            role = session.get('role')
            allowed = ROLE_MODULES.get(role, [])
            if allowed != 'all' and module not in allowed:
                return jsonify({'error': f'Access denied — {module} not available for {role}'}), 403
            return f(*a, **kw)
        return wrapper
    return deco

def _user():
    conn = get_db()
    u = conn.execute("SELECT * FROM users WHERE id=?", (session['uid'],)).fetchone()
    conn.close()
    return row_to_dict(u)

def _audit(action, module, entity, entity_id, details=''):
    u = session.get('name', 'System')
    log_activity(u, action, module, entity, entity_id, details)

# ── AUTH ──────────────────────────────────────────────────────────────
@app.post('/api/login')
def login():
    data = request.get_json(force=True, silent=True) or {}
    conn = get_db()
    u = conn.execute("SELECT * FROM users WHERE email=?", (((data or {}).get('email') or '').strip(),)).fetchone()
    conn.close()
    if not u or not check_password_hash(u['password_hash'], data.get('password', '')):
        return jsonify({'error': 'Invalid email or password'}), 401
    session.clear()
    session['uid'] = u['id']; session['name'] = u['name']; session['role'] = u['role']
    conn = get_db()
    conn.execute("UPDATE users SET last_login=? WHERE id=?", (datetime.utcnow().isoformat(), u['id']))
    conn.commit(); conn.close()
    log_activity(u['name'], 'Login', 'System', 'auth', str(u['id']))
    return jsonify({'ok': True, 'user': {'id': u['id'], 'name': u['name'], 'email': u['email'], 'role': u['role']}})

@app.post('/api/logout')
def logout():
    session.clear()
    return jsonify({'ok': True})

@app.get('/api/me')
@require_login
def me():
    return jsonify({'user': _user()})

# ── DASHBOARD ─────────────────────────────────────────────────────────
@app.get('/api/dashboard')
@require_login
def dashboard():
    conn = get_db()
    def one(q, *a): return conn.execute(q, a).fetchone()[0] or 0
    stats = {
        'projects': one("SELECT COUNT(*) FROM projects"),
        'portfolio': one("SELECT COALESCE(SUM(budget),0) FROM projects"),
        'leads': one("SELECT COUNT(*) FROM leads"),
        'bookings': one("SELECT COUNT(*) FROM bookings"),
        'sales': one("SELECT COALESCE(SUM(price),0) FROM bookings"),
        'invoices': one("SELECT COUNT(*) FROM invoices"),
        'invoices_unpaid': one("SELECT COUNT(*) FROM invoices WHERE status NOT IN ('Paid')"),
        'payments': one("SELECT COUNT(*) FROM payments"),
        'payments_cleared': one("SELECT COALESCE(SUM(amount),0) FROM payments WHERE status='Cleared'"),
        'dues_outstanding': one("SELECT COALESCE(SUM(due),0) FROM dues"),
        'cash_in': one("SELECT COALESCE(SUM(amount),0) FROM transactions WHERE type='Inflow' AND status IN ('Received','Cleared')"),
        'cash_out': one("SELECT COALESCE(SUM(amount),0) FROM transactions WHERE type='Outflow'"),
        'assets_nbv': one("SELECT COALESCE(SUM(cost-accum_dep),0) FROM fixed_assets"),
        'employees': one("SELECT COUNT(*) FROM users"),
    }
    conn.close()
    return jsonify({'stats': stats})

# ── GENERIC CRUD FACTORY ──────────────────────────────────────────────
def _crud(table, module, fields, id_field='id', pk=None):
    def _list():
        conn = get_db()
        q = f"SELECT * FROM {table}"
        args = []
        status = request.args.get('status')
        if status:
            q += f" WHERE status=?"; args.append(status)
        q += " ORDER BY id DESC" if id_field == 'id' else " ORDER BY rowid DESC"
        rows = conn.execute(q, args).fetchall(); conn.close()
        return jsonify(rows_to_dicts(rows))
    def _create():
        data = request.get_json(force=True, silent=True) or {}
        keys = [k for k in fields if k in data]
        vals = [data[k] for k in keys]
        conn = get_db()
        cur = conn.execute(f"INSERT INTO {table}({','.join(keys)}) VALUES({','.join(['?']*len(keys))})", vals)
        conn.commit()
        new_id = cur.lastrowid
        if pk is not None:
            new_id = data.get(pk, new_id)
        conn.close()
        _audit('Created', module, table, str(new_id), json.dumps(data)[:200])
        return jsonify({'ok': True, 'id': str(new_id)}), 201
    def _update(rid):
        data = request.get_json(force=True, silent=True) or {}
        sets = [f"{k}=?" for k in data if k in fields]
        if not sets: return jsonify({'error': 'No valid fields'}), 400
        conn = get_db()
        conn.execute(f"UPDATE {table} SET {','.join(sets)} WHERE {id_field}=?", list(data.values()) + [rid])
        conn.commit(); conn.close()
        _audit('Updated', module, table, str(rid), json.dumps(data)[:200])
        return jsonify({'ok': True})
    def _delete(rid):
        conn = get_db()
        conn.execute(f"DELETE FROM {table} WHERE {id_field}=?", (rid,))
        conn.commit(); conn.close()
        _audit('Deleted', module, table, str(rid))
        return jsonify({'ok': True})
    def _get(rid):
        conn = get_db()
        r = conn.execute(f"SELECT * FROM {table} WHERE {id_field}=?", (rid,)).fetchone()
        conn.close()
        return jsonify(row_to_dict(r) or {'error': 'not found'}), (200 if r else 404)
    return _list, _get, _create, _update, _delete

def _register(table, module, fields, id_field='id', pk=None, perms=('*',)):
    lst, get, cre, upd, dele = _crud(table, module, fields, id_field, pk)
    app.add_url_rule(f'/api/{module}', 'list_' + module, require_module(module)(lst), methods=['GET'])
    app.add_url_rule(f'/api/{module}/<string:rid>', 'get_' + module, require_module(module)(get), methods=['GET'])
    app.add_url_rule(f'/api/{module}', 'create_' + module, require_module(module)(cre), methods=['POST'])
    app.add_url_rule(f'/api/{module}/<string:rid>', 'update_' + module, require_module(module)(upd), methods=['PUT'])
    app.add_url_rule(f'/api/{module}/<string:rid>', 'delete_' + module, require_module(module)(dele), methods=['DELETE'])

_register('leads', 'leads', ['name','phone','email','property','status','priority','type','source','value','owner','next_follow_up','created_at'])
_register('customers', 'customers', ['name','phone','email','property','type','status','dues_num','project'])
_register('projects', 'projects', ['code','name','location','status','progress','budget','manager','type','plots','units'])
_register('dues', 'dues', ['customer','project','unit','total_price','paid','due','due_date','status','bucket','days_overdue','phone'])
_register('fixed_assets', 'assets', ['code','name','category','purchase_date','cost','salvage','useful_life','accum_dep','location','status'], pk='id')

# ── BOOKINGS (string PK) ──────────────────────────────────────────────
@app.get('/api/bookings')
@require_module('bookings')
def list_bookings():
    conn = get_db(); rows = conn.execute("SELECT * FROM bookings ORDER BY date DESC").fetchall(); conn.close()
    return jsonify(rows_to_dicts(rows))

@app.post('/api/bookings')
@require_module('bookings')
def create_booking():
    d = request.get_json(force=True, silent=True) or {}
    conn = get_db()
    mx = conn.execute("SELECT MAX(CAST(REPLACE(id,'BKG-','') AS INTEGER)) FROM bookings").fetchone()[0] or 100
    nid = f"BKG-{int(mx)+1}"
    conn.execute("INSERT INTO bookings(id,client,property,unit,price,advance,status,type,terms,sched_start,date) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                 (nid, d.get('client',''), d.get('property',''), d.get('unit',''), int(d.get('price') or 0),
                  int(d.get('advance') or 0), d.get('status','Pending Review'), d.get('type','Flat'),
                  d.get('terms',''), d.get('sched_start', datetime.utcnow().date().isoformat()),
                  datetime.utcnow().strftime('%b %d, %Y')))
    conn.commit(); conn.close()
    _audit('Created', 'bookings', 'bookings', nid)
    return jsonify({'ok': True, 'id': nid}), 201

@app.put('/api/bookings/<rid>')
@require_module('bookings')
def update_booking(rid):
    d = request.get_json(force=True, silent=True) or {}
    conn = get_db()
    conn.execute("UPDATE bookings SET client=?,property=?,unit=?,price=?,advance=?,status=?,type=?,terms=?,sched_start=? WHERE id=?",
                 (d.get('client',''), d.get('property',''), d.get('unit',''), int(d.get('price') or 0),
                  int(d.get('advance') or 0), d.get('status',''), d.get('type',''), d.get('terms',''),
                  d.get('sched_start',''), rid))
    conn.commit(); conn.close(); _audit('Updated', 'bookings', 'bookings', rid)
    return jsonify({'ok': True})

@app.delete('/api/bookings/<rid>')
@require_module('bookings')
def delete_booking(rid):
    conn = get_db(); conn.execute("DELETE FROM bookings WHERE id=?", (rid,)); conn.commit(); conn.close()
    _audit('Deleted', 'bookings', 'bookings', rid)
    return jsonify({'ok': True})

# ── INVOICES (VAT net computation mirror) ─────────────────────────────
def _inv_net(amount, vat_r, tds_r, ait_r):
    vat = round(amount * vat_r / 100); tds = round(amount * tds_r / 100); ait = round(amount * ait_r / 100)
    return vat, tds, ait, max(0, amount + vat - tds - ait)

@app.get('/api/invoices')
@require_module('invoices')
def list_invoices():
    conn = get_db(); rows = conn.execute("SELECT * FROM invoices ORDER BY issued_date DESC").fetchall(); conn.close()
    return jsonify(rows_to_dicts(rows))

@app.post('/api/invoices')
@require_module('invoices')
def create_invoice():
    d = request.get_json(force=True, silent=True) or {}
    amount = int(d.get('amount') or 0)
    vat_r = int(d.get('vat_rate') or 0); tds_r = int(d.get('tds_rate') or 0); ait_r = int(d.get('ait_rate') or 0)
    vat, tds, ait, net = _inv_net(amount, vat_r, tds_r, ait_r)
    conn = get_db()
    yr = datetime.utcnow().year
    mx = conn.execute("SELECT MAX(CAST(SUBSTR(id,10) AS INTEGER)) FROM invoices WHERE id LIKE ?", (f"INV-{yr}-%",)).fetchone()[0] or 0
    nid = f"INV-{yr}-{int(mx)+1:04d}"
    conn.execute("INSERT INTO invoices(id,client,project,unit,amount,vat_rate,tds_rate,ait_rate,vat,tds,ait,net,challan,status,due_date,issued_date,desc,type) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (nid, d.get('client',''), d.get('project',''), d.get('unit',''), amount, vat_r, tds_r, ait_r,
                  vat, tds, ait, net, d.get('challan',''), d.get('status','Draft'), d.get('due_date',''),
                  d.get('issued_date', datetime.utcnow().date().isoformat()), d.get('desc',''), 'Sales'))
    conn.commit(); conn.close()
    _audit('Created', 'invoices', 'invoices', nid, f"net={net}")
    return jsonify({'ok': True, 'id': nid, 'vat': vat, 'tds': tds, 'ait': ait, 'net': net}), 201

# ── PAYMENTS (ripple mirror: invoice status + dues + txn) ─────────────
def _recompute_invoice(conn, inv_id):
    row = conn.execute("SELECT * FROM invoices WHERE id=?", (inv_id,)).fetchone()
    if not row: return
    paid = conn.execute("SELECT COALESCE(SUM(amount),0) FROM payments WHERE invoice_id=? AND status='Cleared'", (inv_id,)).fetchone()[0]
    net = row['net'] or row['amount']
    status = 'Paid' if paid >= net else ('Partial' if paid > 0 else ('Overdue' if row['status'] == 'Overdue' else ('Draft' if row['status'] == 'Draft' else 'Sent')))
    conn.execute("UPDATE invoices SET status=? WHERE id=?", (status, inv_id))

@app.post('/api/payments')
@require_module('payments')
def create_payment():
    d = request.get_json(force=True, silent=True) or {}
    amount = int(d.get('amount') or 0)
    conn = get_db()
    mx = conn.execute("SELECT MAX(CAST(REPLACE(id,'PAY-','') AS INTEGER)) FROM payments").fetchone()[0] or 0
    pid = f"PAY-{int(mx)+1:03d}"
    inv_id = d.get('invoice_id') or None
    conn.execute("INSERT INTO payments(id,invoice_id,client,amount,date,method,reference,status,notes) VALUES(?,?,?,?,?,?,?,?,?)",
                 (pid, inv_id, d.get('client',''), amount, d.get('date', datetime.utcnow().date().isoformat()),
                  d.get('method','Bank Transfer'), d.get('reference',''), d.get('status','Cleared'), d.get('notes','')))
    if inv_id and amount > 0:
        _recompute_invoice(conn, inv_id)
        # dues ripple
        client = d.get('client','')
        if client:
            due = conn.execute("SELECT * FROM dues WHERE customer=?", (client,)).fetchone()
            if due:
                new_due = max(0, due['due'] - amount)
                status = 'Paid' if new_due <= 0 else 'Upcoming'
                bucket = 'Cleared' if new_due <= 0 else 'On Track'
                conn.execute("UPDATE dues SET paid=paid+?, due=?, status=?, bucket=?, days_overdue=0 WHERE id=?",
                             (amount, new_due, status, bucket, due['id']))
        # cash-flow transaction
        conn.execute("INSERT INTO transactions(id,date,desc,client,project,type,category,status,amount) VALUES(?,?,?,?,?,?,?,?,?)",
                     (f"RCP-{1000+int(mx)+1}", d.get('date', datetime.utcnow().date().isoformat()),
                      f"Payment - {d.get('client','')}", d.get('client',''), '', 'Inflow', 'Payment Received', 'Received', amount))
    conn.commit(); conn.close()
    _audit('Created', 'payments', 'payments', pid, f"amount={amount}")
    return jsonify({'ok': True, 'id': pid}), 201

@app.put('/api/payments/<rid>')
@require_module('payments')
def update_payment(rid):
    d = request.get_json(force=True, silent=True) or {}
    conn = get_db()
    conn.execute("UPDATE payments SET invoice_id=?,client=?,amount=?,date=?,method=?,reference=?,status=?,notes=? WHERE id=?",
                 (d.get('invoice_id'), d.get('client',''), int(d.get('amount') or 0), d.get('date',''),
                  d.get('method','Bank Transfer'), d.get('reference',''), d.get('status',''), d.get('notes',''), rid))
    if d.get('invoice_id'):
        _recompute_invoice(conn, d['invoice_id'])
    conn.commit(); conn.close(); _audit('Updated', 'payments', 'payments', rid)
    return jsonify({'ok': True})

# ── LICENSE ───────────────────────────────────────────────────────────
@app.get('/api/license')
@require_module('license')
def get_license():
    conn = get_db(); r = conn.execute("SELECT * FROM license WHERE id=1").fetchone(); conn.close()
    lic = row_to_dict(r)
    lic['installments'] = json.loads(lic.get('installments') or '[]')
    lic['checklist'] = json.loads(lic.get('checklist') or '[]')
    lic['paid'] = sum(i['amount'] for i in lic['installments'] if i['status'] == 'Paid')
    lic['pct'] = round(lic['paid'] / lic['contract'] * 100) if lic['contract'] else 0
    return jsonify(lic)

@app.post('/api/license/status')
@require_module('license')
def set_license_status():
    d = request.get_json(force=True, silent=True) or {}
    conn = get_db(); conn.execute("UPDATE license SET status=? WHERE id=1", (d.get('status', 'Active'),)); conn.commit(); conn.close()
    _audit('Updated', 'license', 'license', '1', d.get('status', ''))
    return jsonify({'ok': True})

# ── REPORTS / EXPORTS ─────────────────────────────────────────────────
@app.get('/api/reports/unpaid-invoices')
@require_module('invoices')
def unpaid_invoices():
    conn = get_db()
    rows = conn.execute("SELECT * FROM invoices WHERE status NOT IN ('Paid') ORDER BY due_date").fetchall()
    out = []
    for r in rows:
        paid = conn.execute("SELECT COALESCE(SUM(amount),0) FROM payments WHERE invoice_id=? AND status='Cleared'", (r['id'],)).fetchone()[0]
        out.append({**dict(r), 'paid': paid, 'outstanding': max(0, (r['net'] or r['amount']) - paid)})
    conn.close()
    return jsonify(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
