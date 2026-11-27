# Три варианта надписей на фото колоды (последний слайд, Лила 27.11). python3 var2.py && node var2.js
exec(open("make.py").read())
FOTO = '<img class=a src=foto_koloda_1.jpg style="left:0;top:0;width:1080px;height:1350px;object-fit:cover">'
LOGO = '<div class="logo" style="left:0"><img src=she_logo.png></div>'
v = []
# 1. Журнальный: крупный бордовый текст на светлом верху без плашки; внизу сплошная светлая карточка
v.append('<div class=s>' + FOTO +
  '<div class=a style="left:0;right:0;top:0;height:330px;background:linear-gradient(#EFE6D3 55%,rgba(239,230,211,0))"></div>'
  '<div class=a style="left:0;right:0;top:60px;text-align:center;font:400 104px/1 K;color:#7A1F3D">Напишите «САД»</div>'
  '<div class=a style="left:0;right:0;top:180px;text-align:center;font:400 44px/1 I;letter-spacing:6px;color:#7A1F3D">В КОММЕНТАРИЯХ</div>'
  '<div class=a style="left:120px;right:120px;top:1060px;background:#FFF9F1;border-radius:28px;padding:30px 20px 26px;text-align:center;box-shadow:0 24px 40px -18px rgba(122,31,61,.45)">'
  '<div style="font:400 50px/1.15 H;color:#7A1F3D">и я пришлю вам ссылку на колоду</div>'
  '<div style="font:400 26px/1.4 I;color:#7A6E80;margin-top:8px">Женские метафорические карты ручной работы</div></div>'
  '<div class="logo" style="left:0;bottom:22px"><img src=she_logo.png style="height:60px"></div></div>')
# 2. Записки на фото: белые листки на скотче, текст от руки — как записка на фото в образце @chudsgn
v.append('<div class=s>' + FOTO +
  '<div class=a style="left:50%;top:60px;margin-left:-330px;width:660px;background:#FFFDF9;padding:34px 20px 30px;transform:rotate(-2deg);text-align:center;box-shadow:0 20px 30px -16px rgba(0,0,0,.35)">'
  '<i class=tape style="left:50%;top:-20px"></i><div style="font:400 76px/1 H;color:#7A1F3D">Напишите «САД»</div>'
  '<div style="font:400 34px/1.3 I;color:#7A6E80;margin-top:6px">в комментариях</div></div>'
  '<div class=a style="left:50%;top:1070px;margin-left:-360px;width:720px;background:#F4C3D3;padding:30px 20px 26px;transform:rotate(1.5deg);text-align:center;box-shadow:0 20px 30px -16px rgba(0,0,0,.35)">'
  '<i class=pin></i><div style="font:400 56px/1.1 H;color:#7A1F3D">и я пришлю вам ссылку на колоду</div>'
  '<div style="font:400 26px/1.4 I;color:#7A1F3D;margin-top:6px">Женские метафорические карты ручной работы</div></div></div>')
# 3. Рамка: фото в середине, сверху и снизу сплошные светлые поля, текст никогда не лежит на картах
v.append('<div class=s style="background:#FBF5EE">'
  '<img class=a src=foto_koloda_1.jpg style="left:40px;top:250px;width:1000px;height:820px;object-fit:cover;object-position:50% 45%;border-radius:22px">'
  '<div class=a style="left:0;right:0;top:70px;text-align:center;font:400 84px/1 K;color:#7A1F3D">Напишите «САД»</div>'
  '<div class=a style="left:0;right:0;top:170px;text-align:center;font:400 34px/1 I;letter-spacing:5px;color:#C2668A">В КОММЕНТАРИЯХ</div>'
  '<div class=a style="left:0;right:0;top:1100px;text-align:center;font:400 54px/1.1 H;color:#7A1F3D">и я пришлю вам ссылку на колоду</div>'
  '<div class=a style="left:0;right:0;top:1180px;text-align:center;font:400 26px I;color:#7A6E80">Женские метафорические карты ручной работы</div>'
  '<div class="logo" style="left:0;bottom:18px"><img src=she_logo.png style="height:56px"></div></div>')
v[1] = v[1][:-6] + LOGO + '</div>'
open("var2.html", "w").write(f'<html><head><meta charset="utf-8"><style>{css}body{{width:1080px}}</style></head><body>{"".join(v)}</body></html>')
