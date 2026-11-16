// Собирает две версии: SHE_brendbuk_A4.pdf (компьютер/iPad) и SHE_brendbuk_telefon.pdf
const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{
  const b=await chromium.launch();
  const p=await b.newPage();
  const url='file://'+__dirname+'/brandbook.html';
  // A4
  await p.goto(url,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
  const ov=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((pg,i)=>{const r=pg.getBoundingClientRect();let m=0;pg.querySelectorAll('*').forEach(e=>{if(e.closest('.foot')||e.closest('.moon')||e.closest('.st'))return;const q=e.getBoundingClientRect();if(q.height&&q.bottom-r.top>m)m=q.bottom-r.top});return (i+1)+':'+Math.round(m/r.height*297)}));
  console.log('A4 высота контента, мм:',ov.join(' '));
  await p.pdf({path:__dirname+'/SHE_brendbuk_A4.pdf',preferCSSPageSize:true,printBackground:true});
  // телефон
  await p.goto(url,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
  const css=fs.readFileSync(__dirname+'/mobile.css','utf8');
  await p.evaluate(css=>{
    document.body.className='m';
    const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
    document.querySelectorAll('table').forEach(t=>{
      const hs=[...t.querySelectorAll('th')].map(h=>h.textContent.trim());
      if(!hs.length)return;
      t.querySelectorAll('tr').forEach(tr=>[...tr.children].forEach((td,i)=>{if(td.tagName==='TD'&&hs[i])td.dataset.l=hs[i]}));
    });
  },css);
  await p.pdf({path:__dirname+'/SHE_brendbuk_telefon.pdf',preferCSSPageSize:true,printBackground:true});
  await b.close();
})();
