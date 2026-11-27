# Три варианта последнего слайда (Лила 27.11): жёлтый светлее, как на плашках (#F3DFA6). python3 var.py && node var.js
exec(open("make.py").read())
SP2 = SPARK.replace("#E8B93A", "#EBCF7E")
def sp(w, x, y): return f'<div class=stk style="left:{x}px;top:{y}px">{SP2.replace("{w}", str(w))}</div>'
LOGO = '<div class="logo" style="left:0"><img src=she_logo.png></div>'
CTA = f'<div class="a strips" style="left:0;right:0;top:70px;align-items:center">{strip("Напишите «САД»", 0, -1.5, 76)}{strip("в комментариях", 1, 1.5, 76)}</div>'
BOTTOM = '<p class="a small" style="left:0;right:0;top:1190px;text-align:center">Женские метафорические карты ручной работы</p>'
v = []
# 1. Светлый ореол: коробка на бледно-жёлтом круге, пунктирное кольцо, звёздочки
v.append('<div class=s>' + CTA +
  '<div class=a style="left:50%;margin-left:-350px;top:330px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,#FFF8E2 0%,#F8EBC4 55%,#F3DFA6 100%)"></div>'
  '<div class=a style="left:50%;margin-left:-380px;top:300px;width:760px;height:760px;border-radius:50%;border:3px dashed #E2B7C6"></div>'
  '<img class=a src=box_sad.png style="left:50%;top:400px;height:520px;transform:translateX(-50%);filter:drop-shadow(0 24px 30px rgba(122,31,61,.28))">'
  + sp(60, 170, 330) + sp(40, 860, 380) + sp(48, 870, 900) + sp(32, 210, 960) +
  '<div class="a oval" style="left:50%;top:1075px;transform:translateX(-50%) rotate(-2deg);white-space:nowrap;padding:18px 40px">и я пришлю вам ссылку на колоду</div>'
  + BOTTOM + LOGO + '</div>')
# 2. Скрапбук: белый лист со скрепкой, коробка приклеена скотчем, подпись от руки
v.append('<div class=s>'
  '<div class=a style="left:110px;top:120px;width:860px;height:1040px;background:#FFFDF9;transform:rotate(-1.5deg);box-shadow:0 24px 40px -20px rgba(122,31,61,.4)"></div>'
  '<div class=a style="left:150px;top:70px">' + CLIP.replace("width=46 height=115", "width=60 height=150") + '</div>'
  '<div class=a style="left:0;right:0;top:190px;text-align:center;font:400 84px/1 H;color:#7A1F3D">Напишите «САД»</div>'
  '<div class=a style="left:0;right:0;top:290px;text-align:center">' + strip("в комментариях", 2, 1.5, 64) + '</div>'
  '<div class=a style="left:50%;margin-left:-250px;top:440px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,#FFF6DA 0%,#F7E7BA 50%,transparent 72%)"></div>'
  '<img class=a src=box_sad.png style="left:50%;top:440px;height:480px;transform:translateX(-50%) rotate(3deg);filter:drop-shadow(0 20px 26px rgba(122,31,61,.25))">'
  '<i class=tape style="left:600px;top:430px;transform:translateX(-50%) rotate(8deg)"></i>'
  + stk(FLOWER, 110, 170, 820, -10) + stk(HEART, 80, 820, 470, 12) + sp(44, 830, 820) +
  '<div class=a style="left:0;right:0;top:965px;text-align:center;font:400 54px/1.15 H;color:#C2668A">и я пришлю вам ссылку на колоду</div>'
  '<div class=a style="left:0;right:0;top:1065px;text-align:center;font:400 28px I;color:#7A6E80">Женские метафорические карты ручной работы</div>'
  + LOGO + '</div>')
# 3. Бордовый финал в горошек: тёмный фон, коробка в светлом сиянии, кремовые надписи
v.append('<div class=s style="background:#7A1F3D radial-gradient(#ffffff40 3px,transparent 3.5px) 0 0/56px 56px">'
  f'<div class="a strips" style="left:0;right:0;top:70px;align-items:center">{strip("Напишите «САД»", 0, -1.5, 76)}{strip("в комментариях", 2, 1.5, 76)}</div>'
  '<div class=a style="left:50%;margin-left:-400px;top:260px;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,#FFF8E4 0%,#FCEFCB 28%,rgba(250,232,190,.5) 45%,transparent 66%)"></div>'
  '<img class=a src=box_sad.png style="left:50%;top:400px;height:520px;transform:translateX(-50%);filter:drop-shadow(0 24px 34px rgba(0,0,0,.35))">'
  + sp(60, 190, 380) + sp(40, 850, 360) + sp(50, 860, 860) + sp(34, 220, 900) +
  '<div class=a style="left:0;right:0;top:1000px;text-align:center"><span style="display:inline-block;font:400 50px/1.1 H;color:#FFF6EE;border:4px dashed #F4C3D3;border-radius:50%;padding:24px 44px;transform:rotate(-2deg)">и я пришлю вам ссылку на колоду</span></div>'
  '<p class="a small" style="left:0;right:0;top:1170px;text-align:center;color:#F4C3D3">Женские метафорические карты ручной работы</p>'
  '<div class="logo" style="left:0"><img src=she_logo.png style="filter:brightness(0) invert(1) opacity(.85)"></div></div>')
open("var.html", "w").write(f'<html><head><meta charset="utf-8"><style>{css}body{{width:1080px}}</style></head><body>{"".join(v)}</body></html>')
