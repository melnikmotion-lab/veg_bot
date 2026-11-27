const {chromium}=require('playwright');const n=require('./n.json');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const k in n){await p.goto('file://'+__dirname+'/'+k+'.html');await p.waitForTimeout(800);
 const s=await p.$$('.s');for(let i=0;i<s.length;i++)await s[i].screenshot({path:`${k}_${i+1}.jpg`,quality:88,type:'jpeg'});}
await b.close()})();
