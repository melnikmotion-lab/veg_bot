# Задание для нейросети: карты в стиле Лилы («Тайный сад»)

## Где делать
**Google Flow**, вкладка «Изображения» (Images). Там же можно в приложении **Gemini**. Обе программы рисуют одной моделью Google, она называется Nano Banana.
Как это работает: вы загружаете свои готовые карты как образцы (во Flow они называются «ингредиенты»), а модель рисует новую картинку в их стиле.
Задание пишем по-английски: так модель понимает точнее. Ниже под каждым заданием перевод.

## Стиль: что я нашла, просмотрев все 40 карт «Тайного сада»
«Язык эмоций» — карты с текстом и цветным свечением, без рисунков. Поэтому стиль для нейросети — это «Тайный сад».

Цвета я посчитала программой по всем 40 картам (доля — сколько места цвет занимает на всех картах вместе):
- **синие и голубые — больше всего, около 45%:** тёмный ночной сине-зелёный #1F4E5B, синий #3D678B и #5785AC, голубой #6FA6C0, #88BED1, бледно-голубой #A9D0D9, почти белый голубой #DDE9EA, бирюза #027890;
- **розовые — около 15%:** #DB6E85, #E38BA0, тёмно-розовый #BA5071, пудровый #DFB7C4, лиловато-серый #9D798A; яркий малиновый — акцентом (двери на 01, фигуры на 28 и 33, фон 35);
- **жёлтые и кремовые — около 14%:** бледно-лимонный #F4E8A4, сливочный #F5E8C5, солнечный #F7DA5C, песочный #E4C8A2, тёплый бежевый #AF906A;
- **зелёные — около 12%:** травяной #86BB88, светло-оливковый #B4CD9E, тёмный зелёный #5F957A, серо-зелёный #CED7CE;
- **красно-коричневые — около 8%:** красный #C14434 (огонь, дракон, платья), коричневый #6D3A2F (корни, деревья, волосы), серо-коричневый #715F5D;
- **чёрный #0F1113** (ночное небо на 01, 02, 07) и **белый #FDFDFC** (свет, вода, облака).

Что повторяется в рисунке:
- контур тонкий и ровный, чаще тёмным оттенком того же цвета, не чёрным; на голубом бывают белые линии (05, 18, 21);
- заливка плоская, свет — мягкое свечение изнутри: солнце, луна, фонари, лучи (13, 19, 21, 29, 32);
- в волосах, траве, корнях видны штрихи, как карандашом;
- фигуры вытянутые, простые лица; часто обнажённые женщины, кожа светлая, бывает смуглая (22, 26);
- образы сказочные, со смыслом: корни и деревья, вода, лотос, луна, руки, двери, цветы;
- белые четырёхконечные звёздочки;
- рисунок до краёв, без рамки и без текста; формат 800×1120, то есть 5:7.

## Как загружать образцы
Давайте 3–6 карт одного настроения с той, что нужна:
- ночь — 19, 27, 01;
- светлый голубой день — 05, 21, 30;
- зелень — 14, 31, 40;
- розовое — 17, 33, 36;
- солнечное жёлтое — 29, 03.
Чтобы доделать карту, первой загрузите её саму, потом 2–3 карты для стиля. Что доделать, пишете вы. Из ответа выбирайте лучшее и просите поправить одно за раз: «make the pink softer», «remove the second figure».

---

## Задание 1. Новая карта по описанию

```
Use the attached cards as the strict style reference. Create ONE new card for the same deck.

Style (match the references exactly):
- hand-drawn digital illustration for a metaphorical card deck
- thin even outlines, usually a darker shade of the fill colour, not black; white line art on light blue areas
- flat colour fills; light is a soft glow from within (sun, moon, lanterns, rays)
- visible pencil-like strokes in hair, grass and roots
- palette from the references: dominant blues (#1F4E5B, #3D678B, #5785AC, #6FA6C0, #88BED1, #A9D0D9, #DDE9EA, teal #027890), pinks (#DB6E85, #E38BA0, #BA5071, #DFB7C4, mauve #9D798A, magenta accents), creams and yellows (#F4E8A4, #F5E8C5, #F7DA5C, #E4C8A2), greens (#86BB88, #B4CD9E, #5F957A), red #C14434, brown #6D3A2F, black night sky #0F1113, white #FDFDFC
- elongated simple figures with simple faces, no realism, no 3D, no photo look
- small white four-pointed sparkles where it fits
- surreal, symbolic, calm mood

Scene: [ОПИСАНИЕ СЦЕНЫ ПО-АНГЛИЙСКИ — например: a woman sitting inside a giant open seashell on the seabed, holding a small glowing pearl to her chest]

Format: vertical card, aspect ratio 5:7, full-bleed illustration, no border, no frame, no text, no letters, no signature.
```

Перевод: «Возьми приложенные карты строгим образцом стиля и нарисуй ОДНУ новую карту для той же колоды. Рисованная цифровая иллюстрация, тонкий контур тёмным оттенком того же цвета, плоская заливка, свет — мягкое свечение изнутри, штрихи карандашом в волосах и траве, палитра из образцов (больше всего синих и голубых, потом розовые, кремовые и жёлтые, зелёные, красный, коричневый, чёрное ночное небо, белый), простые фигуры без реализма, белые четырёхконечные звёздочки, сказочное спокойное настроение. Сцена: […]. Вертикальная карта 5:7, рисунок до краёв, без рамки и без текста.»

## Задание 2. Доделать существующую карту

```
The FIRST attached image is my unfinished card. The other images are style references from the same deck.

Finish the first card. Keep everything that is already drawn exactly as it is: the composition, the figures, the lines and the colours. Only complete the missing parts: [ЧТО ДОРИСОВАТЬ — например: colour the empty background, finish the left hand, add the plants in the bottom corner].

Match the existing drawing: the same ink outlines, the same flat fills with soft gradients, the same palette. No new objects except the ones I listed. No text, no border. Keep the vertical 5:7 format.
```

Перевод: «Первая картинка — моя недоделанная карта, остальные — образцы стиля. Доделай первую карту. Всё, что уже нарисовано, оставь как есть: расположение, фигуры, линии, цвета. Дорисуй только: […]. Те же контуры, заливка и палитра. Ничего лишнего, без текста и рамки, формат 5:7.»
