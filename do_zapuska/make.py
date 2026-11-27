# Список «Что осталось до запуска» с галочками (PDF с полями-флажками). python3 make.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("S", F + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("SB", F + "DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("N", F + "DejaVuSans.ttf"))

WINE, PINK, LIGHT, GREY = HexColor("#7A2342"), HexColor("#E8A0B4"), HexColor("#FCEFF3"), HexColor("#6E5A60")
W, H = A4
M = 48
txt = ParagraphStyle("t", fontName="S", fontSize=11.5, leading=15.5, textColor=HexColor("#2B1B20"))
note = ParagraphStyle("n", parent=txt, fontName="N", fontSize=9, leading=12, textColor=GREY)

SECTIONS = [
  ("От вас", "это можете сделать только вы", [
    ("Дорисовать пять карт «Тайного сада»: 02, 05, 06, 12, 23.",
     "Сейчас они скрыты, в боте 35 карт, а на витрине написано 40. Как пришлёте, открою их."),
    ("Прислать готовую карту 05.", "Она нужна и для каруселей «Тайный сад»."),
    ("Настроить автоответ на слово «САД» в Instagram.",
     "Последний слайд карусели просит написать «САД», и человек ждёт ссылку на колоду."),
    ("Включить кнопку «Open» в @BotFather и прислать снимок с телефона.",
     "Ссылка: she-bot-production.up.railway.app/app?go=all, режим Fullsize. Снимка я ещё не видела."),
    ("Заменить ключ (токен) бота личного пространства.",
     "Вы присылали его в чат 24.11. В @BotFather нажать Revoke, новый ключ я впишу на сервер."),
    ("Одобрить примеры привычек в планере.",
     "Сейчас стоят: «Стакан воды утром», «Прогулка», «Зарядка», «Без телефона перед сном»."),
    ("Записать голос для ролика «к врачу».", "Сценарий: вариант про спешку."),
    ("Назвать день, когда гайд без мяса в VecBot подорожает с $7 до $19.", None),
  ]),
  ("Проверить вместе", "со второго телефона, например мужа", [
    ("Покупка целиком: выбрать продукт → оплатить → скриншот → вы подтверждаете → «Готово!» → личное пространство.",
     "Команды для проверки: /buyers и /reset."),
    ("Подарок: колода, планер, дневник и «Всё вместе».",
     "Пересланное сообщение, экран «Вам подарок», бант, коробка «Всё вместе»."),
    ("Темы в чате бота («SHE» и «Мои продукты»).", None),
    ("Колоды на телефоне: открываются без глюков, коробки 3D видны с первого раза.", None),
  ]),
  ("После запуска", "можно не ждать", [
    ("20 ресурсных карт за 200 карточек дня.",
     "Карты вы нарисуете через 2–3 месяца, выдачу в боте я сделаю к этому времени."),
    ("Отложенные карточки дня: 233, 238, 333, 336, 337, 339.", None),
  ]),
]
DONE = ["Цены во всех продуктах (27.11)", "Подарки с бантом и коробка «Всё вместе»",
        "Оплата через заказ, выдача один раз (24.11)", "Карусели «Тайный сад», 3 штуки по 6 слайдов"]

c = canvas.Canvas("/home/user/veg_bot/do_zapuska/Do_zapuska_SHE.pdf", pagesize=A4)
c.setTitle("Что осталось до запуска SHE")
page = [1]

def bg():
    c.setFillColor(LIGHT); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(white); c.roundRect(M - 18, 36, W - 2 * M + 36, H - 72, 18, fill=1, stroke=0)

def new_page():
    c.showPage(); page[0] += 1; bg(); return H - 70

bg()
y = H - 82
c.setFillColor(WINE); c.setFont("SB", 24); c.drawString(M, y, "Что осталось до запуска")
y -= 22; c.setFont("N", 10); c.setFillColor(GREY)
c.drawString(M, y, "SHE · 27 ноября 2026 · нажмите на квадратик, чтобы поставить галочку")
y -= 14
n = 0
for title, sub, items in SECTIONS:
    y -= 30
    if y < 150: y = new_page()
    c.setFillColor(PINK); c.roundRect(M, y - 6, W - 2 * M, 26, 8, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("SB", 13); c.drawString(M + 12, y + 2, title)
    c.setFont("N", 9.5); c.drawRightString(W - M - 12, y + 3, sub)
    y -= 26
    for text, extra in items:
        n += 1
        p = Paragraph(text, txt); _, h1 = p.wrap(W - 2 * M - 40, 999)
        q = Paragraph(extra, note) if extra else None
        h2 = q.wrap(W - 2 * M - 40, 999)[1] + 3 if q else 0
        if y - h1 - h2 < 60: y = new_page()
        top = y - 6
        c.acroForm.checkbox(name=f"d{n}", x=M + 4, y=top - 16, size=16, buttonStyle="check",
                            borderColor=WINE, fillColor=white, textColor=WINE, borderWidth=1.2,
                            forceBorder=True, checked=False)
        p.drawOn(c, M + 32, top - h1)
        if q: q.drawOn(c, M + 32, top - h1 - h2)
        y = top - h1 - h2 - 10
    y -= 0

y -= 30
if y < 170: y = new_page()
c.setFillColor(HexColor("#B9D7B5")); c.roundRect(M, y - 6, W - 2 * M, 26, 8, fill=1, stroke=0)
c.setFillColor(HexColor("#2F5130")); c.setFont("SB", 13); c.drawString(M + 12, y + 2, "Уже готово")
y -= 30
for i, d in enumerate(DONE):
    c.acroForm.checkbox(name=f"ok{i}", x=M + 4, y=y - 12, size=16, buttonStyle="check",
                        borderColor=HexColor("#2F5130"), fillColor=white, textColor=HexColor("#2F5130"),
                        borderWidth=1.2, forceBorder=True, checked=True)
    c.setFont("S", 11.5); c.setFillColor(HexColor("#2B1B20")); c.drawString(M + 32, y - 8, d)
    y -= 24
c.save()
print("ok", page[0], "стр.")
