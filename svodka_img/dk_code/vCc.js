const dk=document.getElementById('dk');
dk.querySelector('.dkh').outerHTML='<div class="chs-h"><b class="she-w"><i class="she"></i></b><span>метафорические карты</span></div>';
const st=document.createElement('style');st.textContent=`
#dk{padding-top:28px;display:flex;flex-direction:column;justify-content:center;min-height:100vh;box-sizing:border-box;padding-bottom:24px}
#dk .chs-h .she{background:#FDF0C2}
#dk .chs-h .she-w{width:62%;filter:drop-shadow(0 0 8px rgba(253,240,194,.55)) drop-shadow(0 0 20px rgba(253,240,194,.3));animation:none}
#dk .chs-h span{color:#FDF0C2;margin-top:12px;font:400 19px/1 Kurale,serif;letter-spacing:.12em;text-transform:uppercase}
`+CSS;document.head.appendChild(st);
