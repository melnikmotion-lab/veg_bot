var CSS=`
#dk .dkrow{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:26px}
#dk .dkc{background:none;box-shadow:none;padding:0;text-align:center}
#dk .dkc img{width:100%;margin:0 0 10px;filter:drop-shadow(0 16px 16px rgba(90,30,60,.35))}
#dk .dkc b{font:400 22px/1.1 Kurale,serif;color:#FDF0C2;margin:0}
#dk .dkc small{display:block;font:400 14px/1.3 Kurale,serif;color:#FDF0C2;opacity:.85;margin:6px 0 14px;min-height:36px}
#dk .dkb{display:block;width:100%;margin:0 0 10px;border:0;border-radius:999px;padding:14px 6px;font:400 17px Kurale,serif;background:#C46A98;color:#fff;box-shadow:0 12px 22px -12px rgba(120,40,75,.7)}
#dk .dkb.dkl{background:#FCEFF4;color:#9E4A7E}
`;
var HTML=(d,h,s)=>`<div class="dkc"><img src="/static/box_${d}.webp?v=4"><b>${d==='yaz'?'Язык эмоций':'Тайный сад'}</b><small>${s.replace(/[«»]/g,'')}</small>${h?'<button class="dkb">Сделать расклад</button><button class="dkb dkl">Карта дня</button>':'<button class="dkb">Купить — $12</button><button class="dkb dkl">Карта дня</button>'}</div>`;
