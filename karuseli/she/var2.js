const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/var2.html');await p.waitForTimeout(800);
const s=await p.$$('body > .s');let i=0;for(const e of s)await e.screenshot({path:`${__dirname}/var2_${++i}.jpg`,quality:88,type:'jpeg'});await b.close()})();
