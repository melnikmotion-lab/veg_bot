# Расклады «Тайный сад» в стиле SHE по трендовым приёмам из карусели @mama_mozg.
# python3 make.py && node shot.js  → <имя>_NN.jpg
B = "../"  # картинки карт лежат в karuseli/
Q = {  # вопросы к картам (МАК: вопросы себе, без готовых толкований)
 1: ("s1.jpg", ["Куда ведёт эта лестница в вашей жизни?", "Что мешает начать подниматься?", "Какой первый шаг можно сделать сегодня?"]),
 2: ("s2.jpg", ["Куда вы сейчас идёте?", "Что светит вам впереди?", "Что ждёт вас в лодке?"]),
 3: ("s3.jpg", ["Какая из дверей — ваша?", "Что за ней?", "Какую дверь пора закрыть?"]),
}
def qs(k):
    im, q = Q[k]
    return f'<div class=tag>Карта {k}</div><img class=card src={B}{im}><ul>' + "".join(f"<li>{x}</li>" for x in q) + "</ul>"
backs = '<div class=row>' + "".join(f'<div class=bk><img src={B}sb.jpg><b>{k}</b></div>' for k in (1, 2, 3)) + '</div>'
CTA = '''<h1>Какая карта<br>выпала вам?</h1><p class=big>Напишите номер в комментариях</p>
<div class=box>Напишите <b>САД</b> — пришлю ссылку<br>на бесплатную карту дня</div>
<p class=sm>«Тайный сад» — 40 карт с моими рисунками, 18+<br>Вся колода — $15, навсегда</p>'''

C = {
 # Приём «Выберите карту» (pick-a-card) + «удержите палец на точках»
 "1_vyberite": [
  f'<h1>Выберите карту</h1><p class=big>Она подскажет, что вам<br>сейчас важно услышать</p>{backs}<p class=sm>Запомните номер и листайте →</p>',
  qs(1), qs(2), qs(3), CTA],
 # Приём «Листайте и отдаляйте»
 "2_otdalyajte": [
  f'<h1>Что вы видите?</h1><div class=crop style="background-image:url({B}s1.jpg);background-size:340%;background-position:18% 92%"></div><p class=sm>Листайте →</p>',
  f'<h1>А теперь?</h1><div class=crop style="background-image:url({B}s1.jpg);background-size:180%;background-position:20% 85%"></div>',
  f'<h1>Вся карта</h1><img class=card src={B}s1.jpg><p class=big>Правильного ответа нет.<br>Что увидели вы — то про вас.</p>',
  f'<h1>Спросите себя</h1><ul class=wide>' + "".join(f"<li>{x}</li>" for x in Q[1][1]) + '</ul>',
  CTA.replace("Какая карта<br>выпала вам?", "Что вы увидели<br>первым?").replace("Напишите номер в комментариях", "Напишите в комментариях")],
 # Приём «Пройдите по линии» (линия идёт через слайды)
 "3_liniya": "LINE",
}

css = """@font-face{font-family:K;src:url(../kurale.woff2)}@font-face{font-family:I;src:url(../inter-cyr.woff2)}@font-face{font-family:I;src:url(../inter.woff2);unicode-range:U+0000-00FF,U+2000-206F,U+2190-21FF}
*{margin:0;box-sizing:border-box}body{width:1080px;background:#fff}
.s{width:1080px;height:1350px;background:#D9AABA;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;padding:110px 80px 90px;text-align:center;position:relative;overflow:hidden;font-family:I;color:#5a2236}
.she{position:absolute;top:44px;font:60px K;color:#FDF0C2;letter-spacing:6px}
h1{font:400 92px/1.1 K;color:#6E1F3A}.big{font:500 44px/1.35 I}.sm{font:400 32px/1.4 I;color:#6E1F3Acc}
.card{height:660px;border-radius:28px;box-shadow:0 20px 50px rgba(110,31,58,.3);border:10px solid #FDF0C2}
.tag{font:600 40px I;background:#6E1F3A;color:#FDF0C2;padding:12px 40px;border-radius:40px}
ul{list-style:none;display:flex;flex-direction:column;gap:14px}li{font:500 40px/1.3 I;background:#FDF0C2;border-radius:22px;padding:16px 30px;color:#6E1F3A}
.wide li{font-size:50px;padding:30px 40px}
.row{display:flex;gap:36px}.bk{position:relative}.bk img{width:270px;border-radius:20px;box-shadow:0 14px 34px rgba(110,31,58,.3)}
.bk b{position:absolute;left:50%;bottom:-36px;transform:translateX(-50%);width:84px;height:84px;border-radius:50%;background:#6E1F3A;color:#FDF0C2;font:600 46px/84px I}
.crop{width:760px;height:760px;border-radius:28px;border:10px solid #FDF0C2;box-shadow:0 20px 50px rgba(110,31,58,.3)}
.box{font:500 46px/1.35 I;background:#6E1F3A;color:#FDF0C2;padding:30px 50px;border-radius:28px}.box b{font-weight:800;letter-spacing:2px}
.n{position:absolute;bottom:36px;right:56px;font:30px I;color:#fff9}
.wrap{position:relative;width:3240px;height:1350px;display:flex}.wrap .s{flex:none}.lines{position:absolute;inset:0;pointer-events:none}"""

def page(slides):
    return "".join(f'<div class=s><div class=she>SHE</div>{h}<div class=n>{i+1}/{len(slides)}</div></div>' for i, h in enumerate(slides))

import json
n = {}
for name, sl in C.items():
    if sl == "LINE":
        # 3 слайда-панорамы: слева три состояния, линии ведут к трём картам на 3-м слайде, дальше вопросы и CTA
        moods = [("🌀", "каша в голове"), ("🪫", "нет сил"), ("🌫", "не знаю, чего хочу")]
        left = '<h1 style="position:absolute;top:200px;left:0;right:0">Что у вас<br>сейчас?</h1><p class=big style="position:absolute;top:470px;left:0;right:0">Выберите и пройдите<br>по своей линии →</p><div class=moods>' + "".join(
            f'<div class=m style="top:{y}px"><span>{e}</span>{t}</div>' for (e, t), y in zip(moods, (820, 1000, 1180))) + '</div>'
        mid = '<p class=big style="margin-top:-500px">Ещё немного…</p>'
        right = '<div class=cards3>' + "".join(f'<div class=c3 style="top:{y}px"><img src={B}{Q[k][0]}><b>{k}</b></div>' for k, y in zip((2, 1, 3), (330, 680, 1030))) + '</div>'
        # линии: от состояний (x≈520) к картам (x≈2160+…)
        ys = (850, 1030, 1210); ty = (330, 680, 1030)
        paths = "".join(f'<path d="M560 {a} C1300 {a+(260 if i==0 else -200 if i==1 else -60)}, 1700 {b-(300 if i==2 else -150)}, 2400 {b}" />' for i, (a, b) in enumerate(zip(ys, ty)))
        svg = f'<svg class=lines viewBox="0 0 3240 1350" width=3240 height=1350><g fill=none stroke="#6E1F3A" stroke-width=10 stroke-linecap=round stroke-dasharray="2 22">{paths}</g></svg>'
        extra = """.moods{position:absolute;inset:0}.m{position:absolute;left:70px;display:flex;align-items:center;gap:18px;font:500 40px I;color:#6E1F3A;background:#FDF0C2;border-radius:60px;padding:14px 34px 14px 18px}.m span{font-size:52px}
.cards3{position:absolute;inset:0}.c3{position:absolute;left:330px;margin-top:-150px;display:flex;align-items:center;gap:26px}.c3 img{height:300px;border-radius:12px;border:5px solid #FDF0C2}.c3 b{width:76px;height:76px;border-radius:50%;background:#6E1F3A;color:#FDF0C2;font:600 42px/76px I}"""
        top = ''
        rest = [qs(2).replace('Карта 2','🌀 Карта 2'), qs(1).replace('Карта 1','🪫 Карта 1'), qs(3).replace('Карта 3','🌫 Карта 3'),
                CTA.replace("Какая карта<br>выпала вам?", "Какая линия<br>ваша?").replace("Напишите номер в комментариях", "Напишите эмодзи в комментариях")]
        tot = 3 + len(rest)
        pan = "".join(f'<div class=s><div class=she>SHE</div>{h}<div class=n>{i+1}/{tot}</div></div>' for i, h in enumerate([left, mid, top + right]))
        html = f'<div class=wrap>{pan}{svg}</div>' + "".join(f'<div class=s><div class=she>SHE</div>{h}<div class=n>{i+4}/{tot}</div></div>' for i, h in enumerate(rest))
        open(name + ".html", "w").write(f"<html><head><meta charset=utf-8><style>{css}{extra}</style></head><body>{html}</body></html>")
        n[name] = tot
        continue
    open(name + ".html", "w").write(f"<html><head><meta charset=utf-8><style>{css}</style></head><body>{page(sl)}</body></html>")
    n[name] = len(sl)
json.dump(n, open("n.json", "w"))
