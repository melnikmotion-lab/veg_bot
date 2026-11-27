# Карусели «Тайный сад» в стиле SHE (как коробки и приложение: нежный фон, Kurale, воздух, без плашек и обводок).
# python3 make.py && node shot.js
import json
K = "../"  # карты s1–s3 лежат в karuseli/
INK, ROSE, SOFT = "#7A1F3D", "#C2668A", "#7A6E80"

def fan(n=3, w=300, numbers=True):
    rot = {3: (-9, 0, 9)}[n]
    out = ""
    for i, r in enumerate(rot):
        num = f'<i>{i+1}</i>' if numbers else ""
        out += f'<figure style="transform:rotate({r}deg) translateY({abs(r)*3}px)"><img src="back_sad.jpg" style="width:{w}px">{num}</figure>'
    return f'<div class="fan">{out}</div>'

def reveal(k, img, q, sub):
    return (f'<div class="lbl">Карта {k}</div><img class="card" src="{K}{img}">'
            f'<h2>{q}</h2><p>{sub}</p>')

PRODUCT = '''<img class="box" src="box_sad.png">
<h2>«Тайный сад»</h2><p>40 карт, которые я нарисовала сама. 18+</p>
<div class="cta">Напишите <b>САД</b> в комментариях —<br>пришлю ссылку на бесплатную карту дня</div>
<div class="price">вся колода — $15, навсегда</div>'''

C = {
 # Приём «Выберите карту»: обложка-вопрос + колода, второй слайд тоже цепляет (его Instagram показывает при повторе)
 "1_vyberite": [
  f'<div class="lbl">женские метафорические карты</div><h1>Одна из этих<br>карт — ваша</h1>{fan()}<p style="margin-top:60px">Выберите сердцем и листайте</p>',
  f'<h1>Не думайте</h1><p class="big">Какая первой притянула взгляд?<br>Запомните её номер.</p>{fan(w=260)}<div style="height:40px"></div>',
  reveal(1, "s1.jpg", "Куда ведёт ваша лестница?", "Что вы давно хотите начать, но всё ждёте?"),
  reveal(2, "s2.jpg", "Куда вы идёте сейчас?", "Что светит вам впереди, даже если страшно?"),
  reveal(3, "s3.jpg", "Какая дверь — ваша?", "Какую пора открыть, а какую — закрыть?"),
  '<h1>Отправьте<br>подруге</h1><p class="big">Пусть выберет свою карту.<br>А потом расскажете друг другу, что выпало.</p>',
  PRODUCT],
 # Приём «Листайте и отдаляйте»
 "2_otdalyajte": [
  f'<div class="lbl">тест за 10 секунд</div><h1>Что вы видите<br>первым?</h1><div class="crop" style="background-image:url({K}s3.jpg);background-size:300%;background-position:25% 55%"></div><p>Листайте медленно</p>',
  f'<h1>А теперь?</h1><div class="crop" style="background-image:url({K}s3.jpg);background-size:170%;background-position:30% 50%"></div>',
  f'<img class="card" src="{K}s3.jpg"><h2>Что увидели первым —<br>о том и думаете сейчас</h2>',
  '<div class="lbl">спросите себя</div><div class="list"><div><h3>Открытую дверь</h3><p>Куда я давно хочу войти?</p></div><div><h3>Закрытую дверь</h3><p>Что я держу закрытым?</p></div><div><h3>Звёзды и темноту</h3><p>Где мне сейчас нужна тишина?</p></div></div>',
  '<h1>Сохраните</h1><p class="big">Покажите карту близким<br>и сравните, кто что увидел первым.</p>',
  PRODUCT],
 # Классический расклад на три карты
 "3_rasklad": [
  f'<div class="lbl">расклад на три карты</div><h1>Что держит.<br>Что отпустить.<br>Куда идти.</h1>{fan(numbers=False)}<p>Сделайте его вместе со мной</p>',
  f'<div class="row3"><div><img src="back_sad.jpg"><span>что держит</span></div><div><img src="back_sad.jpg"><span>что отпустить</span></div><div><img src="back_sad.jpg"><span>куда идти</span></div></div><p class="big">Задайте себе вопрос<br>и листайте</p>',
  reveal("· что держит", "s2.jpg", "Что держит вас на месте?", "Чего вы ждёте, стоя у воды?"),
  reveal("· что отпустить", "s3.jpg", "Какую дверь пора закрыть?", "Что вы до сих пор держите открытым по привычке?"),
  reveal("· куда идти", "s1.jpg", "Куда ведёт лестница?", "Какой первый шаг наверх можно сделать на этой неделе?"),
  '<h1>Сохраните<br>расклад</h1><p class="big">Через месяц сделайте его снова<br>и посмотрите, что изменилось.</p>',
  PRODUCT],
}

css = f"""@font-face{{font-family:K;src:url(../kurale.woff2)}}@font-face{{font-family:I;src:url(../inter-cyr.woff2)}}@font-face{{font-family:I;src:url(../inter.woff2);unicode-range:U+0000-00FF,U+2000-206F}}
*{{margin:0;box-sizing:border-box}}body{{width:1080px}}
.s{{width:1080px;height:1350px;background:radial-gradient(120% 80% at 50% 30%,#FBF6F8 0%,#F5EEF2 55%,#EEDFE6 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:42px;padding:120px 100px;text-align:center;position:relative;overflow:hidden;font-family:I;color:{SOFT}}}
.logo{{position:absolute;bottom:48px;font:44px K;color:{ROSE};letter-spacing:4px}}.n{{position:absolute;bottom:56px;right:64px;font:26px I;color:#B9AAB4}}
.lbl{{font:500 28px I;letter-spacing:6px;text-transform:uppercase;color:{ROSE}}}
h1{{font:400 104px/1.08 K;color:{INK}}}h2{{font:400 64px/1.15 K;color:{INK}}}h3{{font:400 52px K;color:{INK}}}
p{{font:400 36px/1.45 I}}.big{{font-size:42px}}
.card{{height:700px;border-radius:26px;box-shadow:0 30px 60px -20px rgba(122,31,61,.35)}}
.fan{{display:flex;justify-content:center;gap:0}}.fan figure{{position:relative;margin:0 -14px}}.fan img{{border-radius:20px;box-shadow:0 26px 50px -18px rgba(122,31,61,.4);display:block}}
.fan i{{position:absolute;left:0;right:0;bottom:-70px;font:normal 54px K;color:{INK}}}
.crop{{width:720px;height:720px;border-radius:26px;background-repeat:no-repeat;box-shadow:0 30px 60px -20px rgba(122,31,61,.35)}}
.list{{display:flex;flex-direction:column;gap:56px}}
.row3{{display:flex;gap:34px}}.row3 img{{width:270px;border-radius:18px;box-shadow:0 22px 44px -18px rgba(122,31,61,.4);display:block}}.row3 span{{display:block;margin-top:26px;font:400 38px K;color:{INK}}}
.box{{height:620px;filter:drop-shadow(0 30px 40px rgba(122,31,61,.3))}}
.cta{{font:400 40px/1.4 I;color:{INK}}}.cta b{{font-weight:700;letter-spacing:3px}}.price{{font:400 30px I;color:{SOFT}}}"""

n = {}
for name, sl in C.items():
    body = "".join(f'<div class="s">{h}<div class="logo">SHE</div><div class="n">{i+1}/{len(sl)}</div></div>' for i, h in enumerate(sl))
    open(name + ".html", "w").write(f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')
    n[name] = len(sl)
json.dump(n, open("n.json", "w"))
