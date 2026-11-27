# Карусели «Тайный сад» в стиле SHE. Механика Лилы (27.11): вопрос → выберите 1, 2 или 3 →
# путаные линии идут через слайды 1–3 → каждая приводит к своей карте → карта со значением → реклама колоды.
# python3 make.py && node shot.js
import json, random
INK, ROSE, SOFT = "#7A1F3D", "#C2668A", "#7A6E80"

# вопрос; карты сверху вниз на 3-м слайде (номер, значение, текст); dest[i] — к какой карте ведёт линия i+1
C = {
 "1_izmenit": ("Что резко изменит<br>вашу жизнь?", [
   ("13", "Смелое решение", "Вы давно знаете, чего хотите. Скоро настанет день, когда вы перестанете ждать и сделаете это."),
   ("26", "Новые люди", "Вас заметят. Кто-то протянет вам руку, и с этого человека начнётся новая глава."),
   ("03", "Возвращение к себе", "Вы вспомните, что вам по-настоящему дорого. На этом вы построите всё остальное.")], (2, 0, 1)),
 "2_meshaet": ("Что мешает вам<br>двигаться дальше?", [
   ("34", "Страх", "Он кажется огромным, пока на него не посмотришь прямо. Нитки, которые его держат, тонкие."),
   ("14", "Мысли по кругу", "Вы так много думаете, что запутались. Сделайте один маленький шаг, и станет легче."),
   ("37", "Старые привычки", "Они разрослись, как корни, и закрыли дорогу. Перешагните через одну сегодня.")], (1, 2, 0)),
 "3_nuzhno": ("Что вам сейчас<br>нужнее всего?", [
   ("36", "Отдых", "Тёплая ванна, тишина, время для себя. Дела подождут."),
   ("31", "Отпустить", "Лягте в траву и дайте дню идти самому. Вы держите слишком многое."),
   ("38", "Новое знание", "Ответ есть в книге, на курсе или у человека, который знает больше. Пора учиться.")], (0, 2, 1)),
}

def smooth(pts):  # Catmull-Rom → кривые Безье
    d = f"M{pts[0][0]:.0f} {pts[0][1]:.0f}"
    for i in range(len(pts) - 1):
        p0, p1, p2 = pts[max(i-1, 0)], pts[i], pts[i+1]
        p3 = pts[min(i+2, len(pts)-1)]
        c1 = (p1[0] + (p2[0]-p0[0])/6, p1[1] + (p2[1]-p0[1])/6)
        c2 = (p2[0] - (p3[0]-p1[0])/6, p2[1] - (p3[1]-p1[1])/6)
        d += f" C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {p2[0]:.0f} {p2[1]:.0f}"
    return d

CARD_Y = (130, 500, 870)  # верх карт на 3-м слайде, высота 330
LEVELS = (380, 760, 1140)
def lines(dest, seed):
    rnd = random.Random(seed)
    perms = [p for p in __import__("itertools").permutations(range(3))]
    cols = []; prev = None
    for x in (1250, 1560, 1870, 2180):  # в каждой колонке линии меняются местами — так они путаются
        p = rnd.choice([q for q in perms if q != prev and (prev is None or sum(a != b for a, b in zip(q, prev)) >= 2)])
        cols.append((x, p)); prev = p
    out = ""
    for i in range(3):
        sx = 540 + (i-1)*300
        lane = 1270 - i*60  # внизу обложки у каждой линии своя дорожка, без пересечений
        ey = CARD_Y[dest[i]] + 165
        pts = [(sx, 1060), (sx, lane - 40), (sx + 60, lane), (1000 + i*60, lane)]
        for x, p in cols:
            pts.append((x + rnd.randint(-40, 40), LEVELS[p[i]] + rnd.randint(-50, 50)))
        pts += [(2470, ey), (2560, ey)]
        out += f'<path d="{smooth(pts)}"/>'
    return (f'<svg class=lines viewBox="0 0 3240 1350" width=3240 height=1350><g fill=none stroke="{INK}" '
            f'stroke-width=6 stroke-linecap=round stroke-linejoin=round>{out}</g>'
            + "".join(f'<circle cx="{540+(i-1)*300}" cy="1060" r="10" fill="{INK}"/>' for i in range(3)) + '</svg>')

PRODUCT = '''<img class="box" src="box_sad.png">
<h2>«Тайный сад»</h2><p>40 карт, которые я нарисовала сама. 18+</p>
<div class="cta">Напишите <b>САД</b> в комментариях —<br>пришлю бесплатную карту дня</div>
<div class="price">вся колода — $15, навсегда</div>'''

css = f"""@font-face{{font-family:K;src:url(../kurale.woff2)}}@font-face{{font-family:I;src:url(../inter-cyr.woff2)}}@font-face{{font-family:I;src:url(../inter.woff2);unicode-range:U+0000-00FF,U+2000-206F}}
*{{margin:0;box-sizing:border-box}}body{{width:3240px}}
.s{{width:1080px;height:1350px;background:radial-gradient(120% 80% at 50% 30%,#FBF6F8 0%,#F5EEF2 55%,#EEDFE6 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:44px;padding:120px 100px;text-align:center;position:relative;overflow:hidden;font-family:I;color:{SOFT};flex:none}}
.wrap{{position:relative;width:3240px;height:1350px;display:flex;background:radial-gradient(60% 90% at 30% 30%,#FBF6F8 0%,#F5EEF2 60%,#EEDFE6 100%)}}.wrap .s{{background:none}}
.lines{{position:absolute;inset:0}}
.logo{{position:absolute;bottom:48px;left:0;right:0;font:44px K;color:{ROSE};letter-spacing:4px}}.n{{position:absolute;bottom:56px;right:64px;font:26px I;color:#B9AAB4}}
h1{{font:400 96px/1.1 K;color:{INK}}}h2{{font:400 72px/1.15 K;color:{INK}}}
p{{font:400 38px/1.45 I}}.big{{font-size:44px}}
.card{{height:690px;border-radius:26px;box-shadow:0 30px 60px -20px rgba(122,31,61,.35)}}
.backs{{display:flex;gap:60px}}.backs div{{font:400 60px K;color:{INK}}}.backs img{{width:240px;border-radius:18px;box-shadow:0 24px 44px -18px rgba(122,31,61,.45);display:block;margin-bottom:18px}}
.end{{position:absolute;left:2590px;height:330px;border-radius:16px;box-shadow:0 20px 40px -16px rgba(122,31,61,.4)}}
.box{{height:600px;filter:drop-shadow(0 30px 40px rgba(122,31,61,.3))}}
.cta{{font:400 40px/1.4 I;color:{INK}}}.cta b{{font-weight:700;letter-spacing:3px}}.price{{font:400 30px I;color:{SOFT}}}"""

n = {}
for seed, (name, (q, cards, dest)) in enumerate(C.items()):
    tot = 8
    s1 = (f'<div class="s" style="justify-content:flex-start;padding-top:130px"><h1>{q}</h1>'
          f'<p class="big">Выберите 1, 2 или 3<br>и идите по своей линии</p>'
          f'<div class="backs">' + "".join(f'<div><img src="back_sad.jpg">{i}</div>' for i in (1, 2, 3)) + '</div>'
          "</div>")
    s2 = f'<div class="s" style="justify-content:flex-start;padding-top:110px"><p class="big">Не отрывайте глаз<br>от своей линии</p><div class="n">2/{tot}</div></div>'
    s3 = f'<div class="s"><div class="n">3/{tot}</div></div>'
    ends = "".join(f'<img class="end" src="k/{c[0]}.jpg" style="top:{y}px">' for c, y in zip(cards, CARD_Y))
    pan = f'<div class="wrap">{s1}{s2}{s3}{lines(dest, seed+7)}{ends}</div>'
    rest = [f'<img class="card" src="k/{c}.jpg"><h2>{t}</h2><p>{x}</p>' for c, t, x in cards]
    rest.append('<h2>Какая карта<br>выпала вам?</h2><p class="big">Напишите в комментариях.<br><br>Отправьте подруге —<br>пусть выберет свою.</p>')
    rest.append(PRODUCT)
    body = pan + "".join(f'<div class="s">{h}<div class="logo">SHE</div><div class="n">{i+4}/{tot}</div></div>' for i, h in enumerate(rest))
    open(name + ".html", "w").write(f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')
    n[name] = tot
json.dump(n, open("n.json", "w"))
