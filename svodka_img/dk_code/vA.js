var CSS=`
#dk .dkrow{display:flex;flex-direction:column;gap:16px;margin-top:32px}
#dk .dkc{display:grid;grid-template-columns:118px 1fr;gap:6px 16px;align-items:center;text-align:left;background:#FCEFF4;border-radius:22px;padding:16px 16px 16px 12px;box-shadow:0 16px 26px -14px rgba(120,40,75,.6)}
#dk .dkc img{width:118px;margin:0;grid-row:span 2;filter:drop-shadow(0 8px 10px rgba(70,40,60,.25))}
#dk .dkc b{font:400 24px/1.1 Kurale,serif;color:#9E4A7E;margin:0}
#dk .dkc small{display:block;font:400 14px/1.3 Kurale,serif;color:#9E4A7E;opacity:.85;margin-top:4px}
#dk .dkbs{grid-column:1/-1;display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
#dk .dkbs.one{grid-template-columns:1fr}
#dk .dkb{margin:0;border-radius:14px;padding:13px 6px;font:400 16px Kurale,serif;background:#C46A98;color:#fff;border:0}
#dk .dkb.dkl{background:#FDF0C2;color:#9E4A7E;border:0}
`;
var HTML=(d,h,s)=>`<div class="dkc"><img src="/static/box_${d}.webp?v=4"><div><b>${d==='yaz'?'Язык эмоций':'Тайный сад'}</b><small>${s.replace(/[«»]/g,'')}</small></div><div class="dkbs ${h?'':'one'}">${h?'<button class="dkb">Сделать расклад</button><button class="dkb dkl">Карта дня</button>':'<button class="dkb">Купить — $12</button>'}</div></div>`;
