var CSS=`
#dk .dkrow{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:76px}
#dk .dkc{position:relative;background:#FCEFF4;border-radius:22px;padding:150px 12px 14px;text-align:center;box-shadow:0 16px 26px -14px rgba(120,40,75,.6)}
#dk .dkc img{position:absolute;left:50%;top:-62px;width:138px;transform:translateX(-50%);margin:0;filter:drop-shadow(0 12px 12px rgba(70,40,60,.3))}
#dk .dkc b{font:400 21px/1.1 Kurale,serif;color:#9E4A7E;margin:0}
#dk .dkc small{display:block;font:400 13px/1.3 Kurale,serif;color:#9E4A7E;opacity:.85;margin:6px 0 4px;min-height:34px}
#dk .dkb{margin-top:8px;border-radius:14px;padding:12px 6px;font:400 16px Kurale,serif;background:#C46A98;color:#fff;border:0}
#dk .dkb.dkl{background:#FDF0C2;color:#9E4A7E;border:0}
`;
var HTML=(d,h,s)=>`<div class="dkc"><img src="/static/box_${d}.webp?v=4"><b>${d==='yaz'?'Язык эмоций':'Тайный сад'}</b><small>${s.replace(/[«»]/g,'')}</small>${h?'<button class="dkb">Сделать расклад</button><button class="dkb dkl">Карта дня</button>':'<button class="dkb">Купить — $12</button>'}</div>`;
