const dk=document.getElementById('dk');
dk.querySelector('.dkh').outerHTML='<div class="chs-h"><b class="she-w"><i class="she" aria-label="SHE"></i></b><span>метафорические карты</span></div>';
const st=document.createElement('style');st.textContent=`
#dk{padding-top:28px;display:flex;flex-direction:column;justify-content:center;min-height:100vh;box-sizing:border-box;padding-bottom:28px}
#dk .chs-h .she{background:#FDF0C2}
#dk .chs-h .she-w{width:74%;filter:drop-shadow(0 0 8px rgba(253,240,194,.55)) drop-shadow(0 0 20px rgba(253,240,194,.3));animation:none}
#dk .chs-h span{color:#FDF0C2;margin-top:14px;font:400 19px/1 Kurale,serif;letter-spacing:.12em;text-transform:uppercase}
`+CSS;document.head.appendChild(st);
const sub={yaz:'«60 карт о чувствах и эмоциях»',sad:'«40 карт, образы о себе настоящей»'};
document.getElementById('dkRow').innerHTML=['yaz','sad'].map(d=>{const h=d==='yaz';return HTML(d,h,sub[d])}).join('');
