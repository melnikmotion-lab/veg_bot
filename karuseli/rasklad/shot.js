const {chromium}=require('playwright');const n=require('./n.json');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const k in n){await p.goto('file://'+__dirname+'/'+k+'.html');await p.waitForTimeout(800);
 const W=await p.$('.wrap');let i=0;
 if(W){const bb=await W.boundingBox();for(let j=0;j<3;j++)await p.screenshot({path:`${__dirname}/${k}_${String(++i).padStart(2,'0')}.jpg`,quality:88,type:'jpeg',fullPage:true,clip:{x:bb.x+j*1080,y:bb.y,width:1080,height:1350}});}
 const s=await p.$$('body > .s');for(const e of s)await e.screenshot({path:`${__dirname}/${k}_${String(++i).padStart(2,'0')}.jpg`,quality:88,type:'jpeg'});}
await b.close()})();
