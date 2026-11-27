# Карусели «Тайный сад» в стиле SHE. Механика Лилы (27.11): вопрос → выберите 1, 2 или 3 →
# линии идут через слайды 1–5, на 3, 4 и 5-м открывается одна карта со значением, 6-й — реклама колоды.
# Дизайн по образцам Лилы с Pinterest (27.11): скрапбук — бумага в клетку, плашки, скотч, скрепки, наклейки.
# python3 make.py && node shot.js
import json, random
INK, ROSE, SOFT = "#7A1F3D", "#C2668A", "#7A6E80"

# вопрос; карты сверху вниз на 3-м слайде (номер, значение, текст); dest[i] — к какой карте ведёт линия i+1
# Значения: у МАК нет заданного смысла, его даёт сам человек (Skillbox, психологи) — поэтому в тексте сначала то, что на карте,
# потом частая трактовка символа (дерево — сам человек и его род), потом вопрос себе. Стиль — Толстой, проще.
C = {
 "1_izmenit": ("Что резко изменит<br>вашу жизнь?", [
   ("13", "Смелое решение", "Это воинская карта, карта победы над страхом и нерешительностью. Карта действия и слов&nbsp;«Я&nbsp;иду вперёд». Пора отбросить сомнения и неподобающее вам малодушие. Какие сомнения вам предстоит отбросить на этой неделе?"),
   ("26", "Перестать притворяться", "Эта карта про лицемерие и усталость от сцены. Клоунесса танцует на шаре в узкой рамке, в сжатой, неестественной позе, и ей хлопают. Пора перестать притворяться, будто вы клоун в цирке, и занять своё естественное место. Перед кем вы притворяетесь?"),
   ("03", "Возвращение к себе", "Эта карта про возвращение к своим корням. Про телесность. Мы перестаём думать, какими должны быть, чтобы угодить другим, и становимся собой, такими, какие мы есть от природы. Отсюда приходят исцеление и сила для тела. Что возвращает вас к себе?")], (2, 0, 1)),
 "2_meshaet": ("Что мешает вам<br>двигаться дальше?", [
   ("34", "Страх", "Эта карта про страх. Красный дракон велик и страшен, а держат его тонкие синие нитки. Страх тоже кажется больше, чем он есть, пока к нему не подойдёшь. Чего вы боитесь сейчас?"),
   ("14", "Мысли по кругу", "Эта карта про мысли, которые ходят по кругу. Стебли оплели женщину в траве так, что её саму не видно. Так бывает, когда долго думаешь об одном. О чём вы думаете по кругу?"),
   ("37", "Старая привычка", "Эта карта про старые привычки. Корни проросли сквозь каменный коридор, и маленькой женщине в красном приходится пробираться между ними. Каждый корень когда-то был тонким. Какая привычка загородила вам дорогу?")], (1, 2, 0)),
 "3_nuzhno": ("Что вам сейчас<br>нужнее всего?", [
   ("36", "Отдых", "Эта карта про отдых. Женщина лежит в ванне с маской на лице, и ей никуда не надо идти. Дела стоят за дверью и подождут. Когда вы отдыхали так в последний раз?"),
   ("31", "Отпустить", "Эта карта про то, чтобы отпустить. Женщина лежит в траве, раскинув руки, и ничего не держит, и от этого ей хорошо. Что вы можете отпустить на этой неделе?"),
   ("38", "Новое знание", "Эта карта про новое знание. Книг так много, что они лежат на полу. Ответ, которого вы ищете, кто-то уже записал. Чему вам пора научиться?")], (0, 2, 1)),
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

# заголовок обложки: строка шрифтом, слово на плашке, конец от руки
Q3 = {"1_izmenit": ("Что резко изменит", "вашу жизнь", "на этой неделе?"), "2_meshaet": ("Что мешает вам", "двигаться дальше", "на этой неделе?"),
      "3_nuzhno": ("Что вам сейчас", "нужнее всего", "на этой неделе?")}
COL = ("#7A1F3D", "#C2668A", "#D9A21B")  # у каждой линии свой цвет: бордовый, розовый, золотой
STRIP = (("#F4C3D3", INK), (INK, "#FFF6EE"), ("#F3DFA6", INK))  # плашки: розовая, бордовая, золотая
BACK_Y = (480, 750, 1020)  # рубашки на обложке сверху вниз, высота 230
LEVELS = (595, 865, 1135)  # уровни линий = высота рубашек
CARD_TOP, CARD_H = 100, 520   # карта на слайдах 3–5
CW = round(CARD_H * 800 / 1118) + 20  # ширина карты с белой рамкой
MID = CARD_TOP + CARD_H // 2  # здесь линия входит в карту
END_X = 300                   # точка, где линия входит в карту (от левого края слайда)

def lines(dest, seed):
    rnd = random.Random(seed)
    perms = list(__import__("itertools").permutations(range(3)))
    last = tuple(2 - d for d in dest)  # на выходе из клубка линии лежат в том порядке, в каком идут к картам
    cols = []; prev = None
    # линии идут ровно до 2-го слайда и путаются дважды — около x=1280 и x=1550, вдали от краёв слайдов
    rev = lambda p, q: all(b == 2 - a for a, b in zip(p, q))  # все три меняются местами — сошлись бы в одной точке
    adj = lambda q: sorted(abs(a - b) for a, b in zip(q, (0, 1, 2))) == [0, 1, 1]  # сначала меняются местами только две соседние линии
    mid = rnd.choice([q for q in perms if adj(q) and q != last and not rev(q, last)])
    cols = [(1250, (0, 1, 2)), (1700, last)]  # одна перестановка — меньше всего пересечений
    out = ""
    for i in range(3):
        d = dest[i]; sy = BACK_Y[i] + 115
        pts = [(345, sy), (700, sy)]
        for x, p in cols:
            pts.append((x + rnd.randint(-20, 20), LEVELS[p[i]] + rnd.randint(-25, 25)))
        ex = 2160 + d * 1080 + END_X
        if d == 0: pts += [(1950, 1135 + rnd.randint(-20, 20)), (2200, 800), (2390, MID), (ex, MID)]
        else:
            top = 80 if d == 1 else 40
            pts += [(1930, LEVELS[2 - d] - 300), (2200 - 100 * d, top), (ex - 330, top), (ex - 140, MID - 80), (ex, MID)]  # подъём наверх — внутри 2-го слайда
        out += (f'<path d="{smooth(pts)}" stroke="{COL[i]}"/><circle cx="345" cy="{sy}" r="13" fill="{COL[i]}"/>'
                f'<circle cx="{ex}" cy="{MID}" r="13" fill="{COL[i]}"/>')
    return (f'<svg class=lines viewBox="0 0 5400 1350" width=5400 height=1350><g fill=none '
            f'stroke-width=9 stroke-linecap=round stroke-linejoin=round>{out}</g></svg>')

CLIP = '<svg class=clip viewBox="0 0 60 150" width=46 height=115><path d="M18 130 V32 a16 16 0 0 1 32 0 V112 a21 21 0 0 1 -42 0 V44" fill=none stroke="#A3949E" stroke-width=6 stroke-linecap=round/></svg>'
HEART = '<svg viewBox="0 0 100 92" width={w}><path d="M50 88C20 65 0 45 12 25 22 8 42 12 50 28 58 12 78 8 88 25 100 45 80 65 50 88Z" fill="#E59AB4"/></svg>'
FLOWER = '<svg viewBox="-50 -50 100 100" width={w}>' + "".join(f'<ellipse rx="15" ry="28" cy="-22" transform="rotate({a})" fill="#F3DFA6"/>' for a in range(0, 360, 72)) + '<circle r="11" fill="#D9A21B"/></svg>'
STAR = '<svg viewBox="-50 -50 100 100" width={w}><g stroke="#C2668A" stroke-width="13" stroke-linecap="round">' + "".join(f'<line y1="-40" y2="40" transform="rotate({a})"/>' for a in (0, 60, 120)) + '</g></svg>'
def stk(svg, w, x, y, r=0): return f'<div class=stk style="left:{x}px;top:{y}px;transform:rotate({r}deg)">{svg.replace("{w}", str(w))}</div>'
def strip(t, k, r, size=84):
    b, c = STRIP[k]
    return f'<span class=strip style="background:{b};color:{c};transform:rotate({r}deg);font-size:{size}px">{t}</span>'

SPARK = '<svg viewBox="-50 -50 100 100" width={w}><path d="M0-48C4-12 12-4 48 0 12 4 4 12 0 48-4 12-12 4-48 0-12-4-4-12 0-48Z" fill="#E8B93A"/></svg>'
def spark(w, x, y): return f'<div class=stk style="left:{x}px;top:{y}px">{SPARK.replace("{w}", str(w))}</div>'
# реклама: сверху призыв, по центру сияющая коробка, снизу что будет; цены и «я нарисовала» нет — люди с карусели меня не знают (Лила 27.11)
# реклама по образцу «конверт» (Pinterest, Лила 27.11): сверху призыв, из открытого конверта по центру сияет коробка,
# на конверте — что будет дальше; цены и «я нарисовала» нет — люди с карусели меня не знают
PRODUCT = (f'<div class="a strips" style="left:0;right:0;top:70px;align-items:center">{strip("Напишите «САД»", 0, -1.5, 76)}{strip("в комментариях", 1, 1.5, 76)}</div>'
           '<div class="a env-flap"></div><div class="a env-back"></div>'
           '<div class="a glow"><i></i></div><img class="a box" src="box_sad.png">'
           '<div class="a env-front"><span>и я пришлю вам<br>ссылку на колоду</span></div>'
           + stk(HEART, 60, 510, 850, -8) + spark(64, 170, 360) + spark(40, 860, 330) + spark(50, 880, 600) + spark(34, 150, 620) +
           '<p class="a small" style="left:0;right:0;top:1140px;text-align:center">Женские метафорические карты ручной работы</p>')

GRID = "linear-gradient(#EFD3DE 2px,transparent 2px),linear-gradient(90deg,#EFD3DE 2px,transparent 2px)"
css = f"""@font-face{{font-family:K;src:url(../kurale.woff2)}}@font-face{{font-family:I;src:url(../inter-cyr.woff2)}}@font-face{{font-family:I;src:url(../inter.woff2);unicode-range:U+0000-00FF,U+2000-206F}}
@font-face{{font-family:H;src:url(../cav5.woff2);unicode-range:U+0400-04FF}}@font-face{{font-family:H;src:url(../cav5l.woff2);unicode-range:U+0000-03FF,U+2000-206F}}
*{{margin:0;box-sizing:border-box}}body{{width:5400px}}
.wrap,.s{{background-color:#FCF6F1;background-image:{GRID};background-size:64px 64px}}
.wrap{{position:relative;width:5400px;height:1350px;font-family:I;color:{SOFT};overflow:hidden}}
.s{{width:1080px;height:1350px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;padding:90px 90px 150px;text-align:center;position:relative;overflow:hidden;font-family:I;color:{SOFT}}}
.lines{{position:absolute;inset:0}}.a{{position:absolute}}
.logo{{position:absolute;bottom:40px;width:1080px;height:76px;text-align:center}}.logo img{{height:76px}}.s .logo{{left:0}}
.n{{position:absolute;bottom:52px;font:26px I;color:#B9AAB4}}
.strips{{display:flex;flex-direction:column;align-items:flex-start;gap:14px}}
.strip{{display:inline-block;font-family:K;line-height:1.15;padding:6px 34px 12px;box-shadow:0 6px 14px -8px rgba(122,31,61,.35)}}
.stk{{position:absolute}}
.tape{{position:absolute;width:150px;height:44px;background:rgba(244,195,211,.8);transform:translateX(-50%) rotate(-4deg)}}
.cw{{position:relative;display:inline-block}}.a.cw{{position:absolute}}
.bk{{position:absolute;left:46px;display:flex;align-items:center;gap:22px}}
.bk b{{font:400 60px/74px K;width:84px;height:84px;text-align:center;border:5px solid;border-radius:50%;transform:rotate(-6deg)}}
.bk img{{height:230px;display:block;border-radius:12px;box-shadow:0 14px 26px -12px rgba(122,31,61,.5)}}
.oval{{font:400 48px/1.1 H;color:{INK};border:4px dashed {ROSE};border-radius:50%;padding:26px 40px;transform:rotate(-3deg)}}
.note{{position:absolute;background:#FFFDF9;box-shadow:0 18px 30px -16px rgba(122,31,61,.35);padding:32px 46px 26px 72px;text-align:left}}
.note .clip{{position:absolute;top:-46px;left:18px}}
.note p{{font:400 30px/1.42 I;color:{SOFT}}}.note .q{{font:400 46px/1.12 H;color:{INK};margin-top:12px}}
.pin{{position:absolute;top:-16px;left:50%;width:34px;height:34px;margin-left:-17px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#E07A9E,#7A1F3D);box-shadow:0 6px 8px rgba(0,0,0,.25)}}
.card{{height:{CARD_H}px;display:block;border:10px solid #fff;box-shadow:0 26px 44px -18px rgba(122,31,61,.45)}}
.box{{height:500px;filter:drop-shadow(0 26px 34px rgba(122,31,61,.3))}}
.ttl{{left:0;top:70px;width:1080px;text-align:center}}.t1{{font:400 80px/1.1 K;color:{INK};margin-bottom:10px}}.t3{{font:400 76px/1 H;color:{ROSE};margin-top:8px}}
.env-back{{left:150px;top:560px;width:780px;height:520px;background:#E7A3BA;border-radius:10px}}.env-flap{{left:150px;top:330px;width:780px;height:240px;background:#DE93AD;clip-path:polygon(0 100%,50% 0,100% 100%)}}.env-front{{left:150px;top:700px;width:780px;height:380px;background:#F4C3D3;border-radius:0 0 10px 10px;clip-path:polygon(0 0,50% 50%,100% 0,100% 100%,0 100%);box-shadow:0 20px 30px -18px rgba(122,31,61,.4)}}.env-front span{{position:absolute;left:0;right:0;bottom:46px;font:400 50px/1.1 H;color:{INK}}}.glow{{left:540px;top:600px;width:0;height:0}}.glow i{{position:absolute;width:880px;height:880px;left:-440px;top:-440px;background:radial-gradient(circle,rgba(255,240,190,1) 0%,rgba(255,222,160,.7) 25%,rgba(244,195,211,.25) 48%,transparent 66%)}}.s .box{{left:50%;top:360px;height:500px;transform:translateX(-50%);filter:drop-shadow(0 0 30px rgba(255,214,120,1)) drop-shadow(0 0 70px rgba(255,214,120,.8))}}
.small{{font:400 30px/1.45 I;color:{SOFT}}}"""

n = {}
for seed, (name, (q, cards, dest)) in enumerate(C.items()):
    tot = 6
    order = [cards[dest.index(k)] for k in range(3)]  # слайд 3 — карта линии, у которой dest=0, и т. д.
    a = []
    q1, q2, q3 = Q3[name]
    a.append(f'<div class="a ttl"><div class=t1>{q1}</div>{strip(q2,0,-1.5,96)}<div class=t3>{q3}</div></div>')
    a.append('<div class="a oval" style="left:660px;top:405px;font-size:38px;padding:20px 34px;text-align:center">выберите<br>1, 2 или 3</div>')
    a.append(stk(HEART, 60, 960, 420, 12))
    a += [f'<div class="bk" style="top:{y}px"><b style="color:{COL[i]};border-color:{COL[i]}">{i+1}</b><img src="back_sad.jpg"></div>' for i, y in enumerate(BACK_Y)]
    a.append('<div class="a" style="left:1150px;top:90px;width:460px;background:#F4C3D3;padding:48px 30px 40px;transform:rotate(-3deg);box-shadow:0 18px 26px -14px rgba(122,31,61,.4);text-align:center;font:400 62px/1.1 H;color:#7A1F3D"><i class=pin></i>Следите за своей линией и листайте →</div>')
    a.append(stk(STAR, 60, 1960, 1180, 10)); a.append(stk(FLOWER, 90, 1150, 1180, 0))
    for k, (c, t, x) in enumerate(order):
        X = 2160 + k * 1080
        body, qq = x.rsplit(". ", 1)
        r = (-2, 2, -1.5)[k]
        a.append(f'<div class="a cw" style="left:{X+540-CW//2}px;width:{CW}px;top:{CARD_TOP}px;transform:rotate({r}deg)"><img class=card src="k/{c}.jpg"><i class=tape style="left:50%;top:-22px"></i></div>')
        a.append(f'<div class="a" style="left:{X}px;width:1080px;top:{CARD_TOP+CARD_H+40}px;text-align:center">{strip(t, k % 3, -r/2, 66)}</div>')
        a.append(f'<div class="note" style="left:{X+110}px;width:860px;top:{CARD_TOP+CARD_H+150}px;transform:rotate({r/3}deg)">{CLIP}<p>{body}.</p><p class=q>{qq}</p></div>')
        a.append(stk([HEART, FLOWER, STAR][k], 64, X + 930, 160, 10))
    a += [f'<div class=logo style="left:{k*1080}px"><img src=she_logo.png></div>' for k in range(5)]
    a += [f'<div class=n style="left:{k*1080+980}px">{k+1}/{tot}</div>' for k in range(1, 5)]
    pan = f'<div class="wrap">{lines(dest, seed+7)}{"".join(a)}</div>'
    last = f'<div class="s">{PRODUCT}<div class="logo"><img src=she_logo.png></div><div class="n" style="right:64px">6/{tot}</div></div>'
    open(name + ".html", "w").write(f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{pan}{last}</body></html>')
    n[name] = tot
json.dump(n, open("n.json", "w"))
