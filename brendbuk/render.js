const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+__dirname+'/brandbook.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const ov=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((pg,i)=>{const r=pg.getBoundingClientRect();let m=0;pg.querySelectorAll('*').forEach(e=>{if(e.closest('.foot')||e.closest('.moon')||e.closest('.st'))return;const q=e.getBoundingClientRect();if(q.height&&q.bottom-r.top>m)m=q.bottom-r.top});return (i+1)+':'+Math.round(m/r.height*297)+'mm'}));
console.log(ov.join(' '));
await p.pdf({path:__dirname+'/SHE_brendbuk.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});await b.close();})();
