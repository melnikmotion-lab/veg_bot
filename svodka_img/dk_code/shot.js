const {chromium}=require('playwright');const fs=require('fs');
const [,,out,mode,cssf]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1});
await p.route(/telegram\.org/,r=>r.abort());
await p.addInitScript(()=>{const cs={};window.Telegram={WebApp:{initData:"x",initDataUnsafe:{user:{id:777}},platform:"ios",version:"8.0",isVersionAtLeast:()=>true,ready(){},expand(){},
setHeaderColor(){},setBackgroundColor(){},setBottomBarColor(){},onEvent(){},offEvent(){},disableVerticalSwipes(){},enableClosingConfirmation(){},
BackButton:{show(){},hide(){},onClick(f){window._bb=f},offClick(){}},MainButton:{show(){},hide(){},setText(){},onClick(){},offClick(){}},
HapticFeedback:{impactOccurred(){},notificationOccurred(){},selectionChanged(){}},
CloudStorage:{getItem(k,c){c(null,cs[k]||"")},getItems(ks,c){const o={};ks.forEach(k=>o[k]=cs[k]||"");c(null,o)},setItem(k,v,c){cs[k]=v;c&&c(null,true)},removeItem(k,c){delete cs[k];c&&c(null,true)},getKeys(c){c(null,Object.keys(cs))}},
openTelegramLink(){},openLink(){},showAlert(m,c){c&&c()},showConfirm(m,c){c(true)},themeParams:{},colorScheme:"light",viewportHeight:844,viewportStableHeight:844}}});
await p.goto('http://localhost:5077/app?go=all');await p.waitForTimeout(2500);
if(mode==='dk'){await p.evaluate(()=>openDk());await p.waitForTimeout(800);}
if(cssf){const s=fs.readFileSync(cssf,'utf8');await p.evaluate(s=>{eval(s)},s);await p.waitForTimeout(1200);}
await p.screenshot({path:out});await b.close();})();
