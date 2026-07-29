import re

f='docs/design-prototype-v4.html'
with open(f,'r') as fp: txt=fp.read()

# 1. ADD renderDocuments + crudDocument AFTER renderSubTable
new_funcs_1 = """}
function renderDocuments(el){
  var q=(document.getElementById('docSearch')||{}).value||'';
  var ft=(document.getElementById('docFType')||{}).value||'';
  var filtered=mockDocuments.filter(function(d){
    if(ft&&d.type!==ft)return false;
    if(q&&!d.title.toLowerCase().includes(q.toLowerCase())&&!d.type.toLowerCase().includes(q.toLowerCase()))return false;
    return true;
  });
  var docTypes=mockDocuments.reduce(function(a,d){if(a.indexOf(d.type)<0)a.push(d.type);return a;},[]);
  var pagD=_pg('documents',filtered);
  el.innerHTML='<div class="fade-in"><div class="page-title">Data Vault</div><div class="page-subtitle">'+mockDocuments.length+' documents \\u00B7 '+mockDocuments.filter(function(d){return d.status==='Verified'}).length+' verified</div>'+
    '<div class="toolbar" style="margin-bottom:6px">'+
      '<input id="docSearch" placeholder="Search documents..." oninput="_PG.documents={page:1,perPage:_pgPerPage};renderModule()" style="padding:4px 8px;border:1px solid #e0e0e0;border-radius:4px;font-size:10px;outline:none;width:160px"/>'+
      '<select id="docFType" onchange="_PG.documents={page:1,perPage:_pgPerPage};renderModule()" style="padding:4px 6px;font-size:9px;border:1px solid #e0e0e0;border-radius:4px"><option value="">All Types</option>'+docTypes.map(function(t){return '<option value="'+t+'">'+t+'</option>';}).join('')+'</select>'+
      '<div class="spacer"></div><button class="action-btn primary" onclick="crudDocument()" style="padding:3px 8px;font-size:10px">+ Upload Document</button>'+
    '</div>'+
    '<div class="card"><div class="card-body" style="padding:0"><div class="table-wrap"><table><thead><tr><th>Title</th><th>Type</th><th>Property</th><th>Date</th><th>Status</th><th></th></tr></thead><tbody>'+
    pagD.items.map(function(d){
      return '<tr style="cursor:pointer" onclick="showToast(\\x27'+d.title+'\\x27,\\'info\\x27)"><td style="font-weight:500">'+d.title+'</td><td><span style="padding:1px 5px;border-radius:3px;font-size:8px;background:#eef3ff;color:#2F80ED">'+d.type+'</span></td><td style="font-size:10px">'+d.property+'</td><td style="font-size:10px">'+d.date+'</td><td><span class="badge-status '+(d.status==='Verified'?'badge-active':'badge-pending')+'">'+d.status+'</span></td><td><span style="color:#2F80ED;cursor:pointer;font-size:11px" onclick="event.stopPropagation();crudDocument(mockDocuments.find(function(x){return x.id==='+d.id+'}))">\\u270E</span> <span style="color:#e53935;cursor:pointer;font-size:11px" onclick="event.stopPropagation();if(confirm(\\x27Delete '+d.title+'?\\x27)){var idx=mockDocuments.findIndex(function(x){return x.id==='+d.id+'});if(idx>=0)mockDocuments.splice(idx,1);DB.save(\\'documents\\x27);showToast(\\'Deleted\\x27,\\'info\\x27);renderModule()}">\\u2715</span></td></tr>';
    }).join('')+
    '</tbody></table>'+_pgHtml('documents',pagD.total,pagD.page,pagD.totalPages,pagD.perPage)+'</div></div></div></div>';
}
function crudDocument(item){
  var n=!item;
  var types=mockDocuments.reduce(function(a,d){if(a.indexOf(d.type)<0)a.push(d.type);return a;},[]);
  var props=['Muktodhara','Jolshiri','Corporate','Both'];
  var d=n?{id:mockDocuments.length+1,title:'',type:types[0]||'CS Khatiyan',property:props[0],date:new Date().toISOString().split('T')[0],status:'Pending Review'}:item;
  openModal(n?'Upload Document':'Edit Document',
    formRow(inputField('Title','df_title',d.title,'',true),selectField('Type','df_type',d.type,types,true))+
    formRow(selectField('Property','df_prop',d.property,props,true),inputField('Date','df_date',d.date))+
    selectField('Status','df_stat',d.status,['Pending Review','Verified','Expired'],true),
    function(){
      var data={id:n?(mockDocuments.length+1):d.id,title:g('df_title'),type:g('df_type'),property:g('df_prop'),date:g('df_date'),status:g('df_stat')};
      if(n){mockDocuments.push(data);DB.save('documents');showToast('Document uploaded','success');}
      else{var idx=mockDocuments.findIndex(function(x){return x.id===d.id});if(idx>=0){mockDocuments[idx]=data;DB.save('documents');showToast('Document updated','info');}}
      renderModule();
    }
  );
}"""

# Find and replace the string "}\n\nlet financeTab" with our new functions + "\n\nlet financeTab"
old_end_subtable = '}\n\nlet financeTab'
new_part1 = new_funcs_1 + '\n\nlet financeTab'
txt = txt.replace(old_end_subtable, new_part1, 1)
print("Step 1 done: added renderDocuments + crudDocument")

# 2. ADD crudVariation + crudBIReport BEFORE </script>
crud_variation_bi = """
function crudVariation(item){
  var n=!item;
  var projects=['Muktodhara Green Park','Jolshiri Abason','Corporate'];
  var v=n?{id:'VO-'+String(mockVariations.length+1).padStart(3,'0'),project:projects[0],title:'',status:'Draft',impact:0,originator:'Site Engineer',date:new Date().toISOString().split('T')[0],schedule:0}:item;
  openModal(n?'New Variation Order':'Edit VO',
    formRow(inputField('Title','v_title',v.title,'',true),selectField('Project','v_proj',v.project,projects,true))+
    formRow(inputField('Cost Impact (\\u09F3)','v_impact',String(v.impact||''),'number',true),inputField('Schedule Impact (days)','v_sched',String(v.schedule||''),'number',true))+
    formRow(selectField('Status','v_stat',v.status,['Draft','Pending Review','Approved','Rejected']),selectField('Originator','v_orig',v.originator,['Site Engineer','Architect','Client','Project Manager','Contractor'],true))+
    inputField('Date','v_date',v.date),
    function(){
      var d={id:v.id,project:g('v_proj'),title:g('v_title'),status:g('v_stat'),impact:'+\\u09F3 '+parseInt(g('v_impact')||0).toLocaleString('en-IN'),originator:g('v_orig'),date:g('v_date')||v.date,schedule:'+'+g('v_sched')+' days'};
      if(n){mockVariations.push(d);DB.save('variations');showToast('VO created','success');}
      else{var idx=mockVariations.findIndex(function(x){return x.id===v.id});if(idx>=0){mockVariations[idx]=d;DB.save('variations');showToast('Updated','info');}}
      renderModule();
    }
  );
}
function crudBIReport(item){
  var n=!item;
  var types=['Chart','Table','Funnel','Bar Chart','Line Chart','Gauge'];
  var r=n?{name:'',type:'Chart',period:new Date().toLocaleDateString('en-US',{month:'short',year:'numeric'}),updated:new Date().toISOString().split('T')[0],status:'Manual'}:item;
  openModal(n?'Generate Report':'Edit Report',
    formRow(inputField('Report Name','br_name',r.name,'',true),selectField('Type','br_type',r.type,types,true))+
    formRow(inputField('Period','br_period',r.period,'',true),selectField('Status','br_stat',r.status,['Manual','Auto'],true)),
    function(){
      var d={name:g('br_name'),type:g('br_type'),period:g('br_period'),updated:new Date().toISOString().split('T')[0],status:g('br_stat')};
      if(n){mockBIReports.push(d);DB.save('bi_reports');showToast('Report generated','success');}
      else{var idx=mockBIReports.findIndex(function(x){return x.name===r.name});if(idx>=0){mockBIReports[idx]=d;DB.save('bi_reports');showToast('Updated','info');}}
      renderModule();
    }
  );
}"""

# Find the LAST occurrence of </script> (the closing script tag)
last_script = txt.rfind('</script>')
if last_script > 0:
    txt = txt[:last_script] + crud_variation_bi + '\n\n' + txt[last_script:]
    print("Step 2 done: added crudVariation + crudBIReport")
else:
    print("ERROR: Could not find </script>")

with open(f,'w') as fp: fp.write(txt)
print(f"Total lines: {len(txt.splitlines())}")
print("ALL DONE!")
