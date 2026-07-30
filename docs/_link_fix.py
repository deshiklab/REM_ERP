#!/usr/bin/env python3
"""Fix grid cells and add cross-linking helpers."""
import sys

with open('/root/REM_ERP/docs/design-prototype-v5.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

changes = []

# === FIX 1: Grid cells - add unit ID to openUnitDetail call ===
# Line 3093 (0-indexed: 3092)
line_idx = 3092  # 0-indexed
line = lines[line_idx]
old_text = "openUnitDetail(\\'" + "' + project.id + '" + "\\')"
new_text = "openUnitDetail(\\'" + "' + project.id + '" + "\\',\\'" + "' + u.id + '" + "\\')"
if old_text in line:
    lines[line_idx] = line.replace(old_text, new_text)
    changes.append("Grid: added unit ID to openUnitDetail (line 3093)")
else:
    print(f"WARN: Grid pattern not found in line 3093")
    print(f"  Looking for: {repr(old_text)}")
    print(f"  Line: {repr(line[:200])}")

# === FIX 2: Add helpers before editUnitStatus ===
helper1 = """function findAndOpenCustomer(name) {
  if (!name) return;
  var entity = mockEntities.find(function(e) { return e.name === name || e.companyName === name; });
  if (entity) { openCustomer(entity.id); return; }
  var lead = mockLeads.find(function(l) { return l.name === name; });
  if (lead) { openLead(lead.id); return; }
  showToast('Customer \"' + name + '\" not found in contacts', 'info');
}
function openBookingByRef(ref) {
  if (!ref) return;
  var booking = mockBookings.find(function(b) { return b.id === ref; });
  if (booking) { openBooking(booking.id); return; }
  showToast('Booking ' + ref + ' not found', 'info');
}
function switchToPropertyUnit(customerName) {
  closeModal();
  for (var pi = 0; pi < mockProperties.length; pi++) {
    var p = mockProperties[pi];
    for (var ui = 0; ui < p.units.length; ui++) {
      if (p.units[ui].customer === customerName) {
        var pu = p.units[ui];
        propFilter = p.id;
        propUnitTab = 'grid';
        switchModule('properties_units');
        setTimeout('openUnitDetail(\"' + p.id + '\",\"' + pu.id + '\")', 400);
        return;
      }
    }
  }
  switchModule('properties_units');
}
"""

# Insert before editUnitStatus
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped == 'function editUnitStatus(projId, unitId) {':
        lines.insert(i, helper1)
        changes.append(f"Added 3 helper functions before editUnitStatus (line {i+1})")
        break

# === FIX 3: Add View Unit button to booking modal ===
for i, line in enumerate(lines):
    if "function openBooking(id){" in line:
        # Find the Close button in the modal footer
        for j in range(i, min(i+100, len(lines))):
            if "Close</button>'" in lines[j] and "onclick=" in lines[j]:
                old_btn = lines[j].strip()
                # Add View Unit button before Close
                lines[j] = lines[j].replace(
                    "<button onclick=\"closeModal()\">Close</button>",
                    "<button class=\"drawer-btn\" onclick=\"closeModal();switchToPropertyUnit('" + "' + b.client + '" + "')\">View Unit</button><button onclick=\"closeModal()\">Close</button>"
                )
                changes.append(f"Added View Unit button to booking modal (line {j+1})")
                break
        break

# === FIX 4: Enhance customer properties tab ===
# Add linked inventory units section
for i, line in enumerate(lines):
    if "}else if(tab==='properties'){" in line:
        # Find where to insert - after the stats row and project list
        for j in range(i, min(i+40, len(lines))):
            if "No projects assigned" in lines[j] or "No properties" in lines[j]:
                # Insert after this line
                unit_section = """    '<div style="margin-top:10px"><h3 style="font-size:11px;font-weight:600;color:#555;margin-bottom:6px">Inventory Units</h3>' +
    (function() {
      var displayName = e.type === 'company' ? e.companyName : e.name;
      var linked = [];
      mockProperties.forEach(function(p) {
        p.units.forEach(function(u) {
          if (u.customer === displayName) linked.push({proj: p, unit: u});
        });
      });
      if (!linked.length) return '<div style="padding:8px;text-align:center;font-size:10px;color:#999">No linked inventory units</div>';
      return '<div style="display:flex;gap:4px;flex-wrap:wrap">' + linked.map(function(l) {
        var cols = {Available:'#4caf50', Booked:'#2196f3', Reserved:'#ff9800', Sold:'#e53935'};
        var c = cols[l.unit.status] || '#999';
        return '<div style="cursor:pointer;padding:6px 8px;border:1px solid ' + c + ';border-radius:6px;background:' + c + '10;font-size:10px" onclick="propFilter=\\'' + "' + l.proj.id + '" + '\\';switchModule(\\'properties_units\\');setTimeout(function(){openUnitDetail(\\'' + "' + l.proj.id + '" + '\\',\\'' + "' + l.unit.id + '" + '\\')},400)">' +
        '<div style="font-weight:600;color:' + c + '">' + l.proj.name + ' - ' + l.unit.number + '</div>' +
        '<div style="font-size:8px;color:#888">' + l.unit.type + ' \u00b7 ' + l.unit.size + ' \u00b7 ' + l.unit.status + '</div></div>';
      }).join('') + '</div>';
    })() +
"""
                lines.insert(j+1, unit_section)
                changes.append(f"Added inventory units section to customer properties tab (line {j+2})")
                break
        break

# Write back
with open('/root/REM_ERP/docs/design-prototype-v5.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("\n=== CHANGES ===")
for c in changes:
    print(c)
print(f"\nFile: {len(lines)} lines")
