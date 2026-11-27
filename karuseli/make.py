# Карусели SHE: каждый слайд 1080x1350. Слайд = (картинка или '', текст сверху, текст снизу)
import json
C = {
 "1_yazyk_emocij": [
  ("backs", "Выберите карту:<br>1, 2 или 3", "Запомните число и листайте →"),
  ("y1.jpg", "Карта 1", ""),
  ("y2.jpg", "Карта 2", ""),
  ("y3.jpg", "Карта 3", ""),
  ("", "Ответьте себе на вопрос<br>с вашей карты", "А в комментариях напишите,<br>какое число выбрали"),
  ("yb.jpg", "Карта дня —<br>бесплатно", "В боте SHE, ссылка в шапке профиля.<br>Вся колода «Язык эмоций» — $12, навсегда"),
 ],
 "2_tajnyj_sad": [
  ("s1.jpg", "Что вы видите<br>на этой карте?", "Напишите первое, что пришло в голову"),
  ("", "Правильного ответа<br>здесь нет", "Каждая видит в карте своё.<br>Так работают метафорические карты"),
  ("s2.jpg", "А здесь?", ""),
  ("s3.jpg", "Какую дверь<br>вы бы открыли?", ""),
  ("sb.jpg", "«Тайный сад»", "40 женских метафорических карт<br>с моими авторскими иллюстрациями. 18+"),
  ("", "Карта дня —<br>бесплатно", "В боте SHE, ссылка в шапке профиля.<br>Вся колода — $15, навсегда"),
 ],
 "3_planer": [
  ("", "Когда дел столько,<br>что не знаешь,<br>за что хвататься", "листайте →"),
  ("p1.png", "Пишу всё в расписание дня", "Что не успела — переношу<br>на другой день одной кнопкой ↱"),
  ("", "Выбираю одно<br>главное дело", "Сделала его —<br>и день прошёл не зря"),
  ("p2.png", "Привычки отмечаю кружками", "Через месяц видно,<br>что правда стало привычкой"),
  ("pc.jpg", "Первая неделя — бесплатно", "Все функции. Потом весь планер — $20 на год.<br>В боте SHE, ссылка в шапке профиля"),
 ],
 "4_dnevnik": [
  ("", "Мысли крутятся<br>и не дают уснуть?", "листайте →"),
  ("", "Выпишите их", "В Бейлорском университете проверили:<br>кто 5 минут перед сном выписывал дела<br>на завтра, засыпал быстрее"),
  ("d1.png", "Я пишу<br>в «Моём личном дневнике»", "Дата ставится сама.<br>Доступ к вашему дневнику есть только у вас"),
  ("", "Попробуйте один раз —<br>бесплатно", "В боте SHE, ссылка в шапке профиля.<br>Дневник на год — $15"),
 ],
 "5_gajd": [
  ("", "«Где ты берёшь белок?»", "Меня спрашивают об этом всю жизнь.<br>Я ни разу не ела мясо, рыбу и яйца"),
  ("", "Белка нужно около 1 г<br>на 1 кг веса", "Я вешу 63 кг —<br>мне нужно 63 г белка в день"),
  ("", "Мой завтрак — 37 г белка", "Овсянка 100 г · творог 100 г<br>ложка чиа · 15 г миндаля"),
  ("", "Главная ошибка —<br>просто убрать мясо", "Питание нужно перестроить целиком,<br>тогда в нём всего хватит"),
  ("", "Всё это — в моём гайде", "Как посчитать свою норму, таблицы продуктов,<br>4 меню на день и 13 моих рецептов.<br>$19 · ссылка в шапке профиля"),
 ],
}
css = """@font-face{font-family:K;src:url(kurale.woff2)}@font-face{font-family:I;src:url(inter-cyr.woff2)}
*{margin:0;box-sizing:border-box}body{width:1080px}
.s{width:1080px;height:1350px;background:#D9AABA;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:44px;padding:80px;text-align:center;position:relative;overflow:hidden}
.s:before{content:"SHE";position:absolute;top:44px;font:60px K;color:#FDF0C2;letter-spacing:6px}
h1{font:400 78px/1.15 K;color:#6E1F3A}p{font:400 38px/1.4 I;color:#5a2236}
img{max-width:820px;max-height:680px;border-radius:28px;box-shadow:0 20px 50px rgba(110,31,58,.25)}
.b{display:flex;gap:40px;margin-bottom:110px}.b div{position:relative}.b img{width:280px}.b span{position:absolute;left:0;right:0;bottom:-130px;font:96px K;color:#6E1F3A}
.n{position:absolute;bottom:36px;right:56px;font:30px I;color:#fff9}"""
for name, sl in C.items():
    h = f"<html><head><meta charset=utf-8><style>{css}</style></head><body>"
    for i, (im, t, b) in enumerate(sl):
        if im == "backs":
            pic = '<div class=b>' + ''.join(f'<div><img src=yb.jpg><span>{k}</span></div>' for k in (1, 2, 3)) + '</div>'
        else:
            pic = f"<img src={im}>" if im else ""
        h += f"<div class=s><h1>{t}</h1>{pic}{'<p>' + b + '</p>' if b else ''}<div class=n>{i + 1}/{len(sl)}</div></div>"
    open(name + ".html", "w").write(h + "</body></html>")
json.dump({k: len(v) for k, v in C.items()}, open("n.json", "w"))
