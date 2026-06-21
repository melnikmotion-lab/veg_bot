import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ID группы куда приходят уведомления об оплате
ADMIN_GROUP_ID = -1003987805583

# ── Тексты ────────────────────────────────────────────────────────────────────

GUIDE_TEXT = """Привет! Очень рада, что тебя заинтересовал мой гайд по вегетарианскому правильному питанию: без мяса, рыбы и яиц 🌱

Это большой, подробный гайд на 45 страниц, в котором собрана вся база, чтобы наконец выстроить простое, вкусное, сбалансированное питание без хаоса в бесконечном количестве разрозненных советов по питанию, которые непонятно как собрать в одну систему, догадок как закрыть дефициты и бесконечных часов у плиты.

Что ты получишь внутри:

1. Поймёшь, как питаться действительно сбалансированно

Разберёшься, как составлять рацион так, чтобы получать достаточно белков, жиров и углеводов, чувствовать сытость, энергию и лёгкость.

Научишься выстраивать свою систему питания, которую реально сможешь воплотить в жизнь, а так же научишься рассчитывать питание под себя:

С учетом:
• веса
• образа жизни
• уровня активности
• целей (похудение / набор веса / поддержание)

Узнаешь как это рассчитать в будущем, если эти факторы поменяются.

И главное — поймёшь, почему без этого невозможно выстроить грамотное питание.

⸻

2. Узнаешь, как избежать дефицитов на вегетарианстве

Разберём:
• какие дефициты бывают чаще всего
• как их предупредить
• какие анализы важны
• где брать белок, если не есть мясо
• как сделать рацион полноценным

⸻

3. Получишь готовые варианты меню

Несколько примеров сбалансированного меню, которые можно легко адаптировать под себя и свои вкусы.

Ты поймёшь сам принцип построения рациона и перестанешь постоянно начинать "правильное питание с понедельника", не понимая, как сделать его частью жизни.

⸻

4. Вегетерианка с опытом жизни без мяса с рождения, поделится с тобой самыми любимыми, лучшими и вкусными рецептами на каждый день 🌱

Там будут как простые рецепты, так и рецепты для особого повода.

Вот некоторые из них:
• высокобелковые супы
• вкуснейший наваристый борщ без мяса
• вегетарианская лазанья
• экзотические индийские блюда
• рецепт бобовых котлет в 5 разных вариациях, фактически получая 5 разных по вкусу и простых рецептов
• сладкие и солёные сырники без яиц
• бутерброды со шпротами без рыбы

⸻

5. Удобные таблицы продуктов

Для простого составления рациона ты получишь таблицы с содержанием белков, жиров, углеводов и других важных веществ в продуктах.

⸻

Этот гайд для тебя, если ты хочешь:

✔ перейти на вегетарианское питание и не знаешь как питаться сбалансированно
✔ не тратить часы на готовку для того что бы питаться хорошо
✔ похудеть / набрать вес экологично
✔ ты давно вегетарианишь, но не знаешь как сделать питание здоровым, у тебя нет системы и понимания что нужно твоему телу

⸻

После прочтения у тебя будет чёткое понимание, как кормить своё тело качественно, получать удовольствие от еды и жить без постоянных мыслей: "что бы такого съесть полезного".

Это не просто сборник рецептов — это система питания, которую ты сможешь использовать всю жизнь 🌱

💵 Стоимость — 7$"""

PAYMENT_TEXT = "Выбери удобный способ оплаты ниже: 💳✨"

PAYPAL_TEXT = """💻 <b>Оплата через PayPal</b>

Переведи 7$ на:
📧 <code>jagannathastaka108@gmail.com</code>

После оплаты нажми кнопку ниже и пришли скрин платежа 🧾"""

UKRAINE_TEXT = """🇺🇦 <b>Украинская карта</b>

• Отримувач: ФОП Мельнік Ліла Дмитрівна
• IBAN: <code>UA783220010000026001370116413</code>
• ІПН/ЄДРПОУ: <code>3752610508</code>
• Банк: Акціонерне товариство УНІВЕРСАЛ БАНК
• МФО: <code>322001</code>
• ЄДРПОУ Банку: <code>21133352</code>
• Назначення платежа: гайд

После оплаты нажми кнопку ниже и пришли скрин платежа 🧾"""

CRYPTO_TEXT = """💎 <b>Криптовалюта (USDT TRC20)</b>

Переведи 7$ в TRC20 на:
<code>TPstMKR5HbdC4d6hEntWQ7BnD9iTjpxZ1Y</code>

После оплаты нажми кнопку ниже и пришли скрин платежа 🧾"""


GEORGIA_TEXT = """🇬🇪 <b>Грузинская карта (Bank of Georgia)</b>
Принимает международные переводы 🌍

<b>Перевод в долларах (USD):</b>
• Intermediary bank: Citibank N.A., New York, USA; SWIFT: CITIUS33
• Bank: Bank of Georgia, SWIFT: BAGAGE22
• Получатель: MELNIK OLEKSII
• Счёт: <code>GE87BG0000000609223652</code>

<b>Перевод в евро (EUR):</b>
• Intermediary bank: Commerzbank, Frankfurt, Germany; SWIFT: COBADEFF
• Bank: Bank of Georgia, SWIFT: BAGAGE22
• Получатель: MELNIK OLEKSII
• Счёт: <code>GE87BG0000000609223652</code>

<b>Перевод в фунтах (GBP):</b>
• Intermediary bank: Citibank N.A., London, UK; SWIFT: CITIGB2L
• Bank: Bank of Georgia, SWIFT: BAGAGE22
• Получатель: MELNIK OLEKSII
• Счёт: <code>GE87BG0000000609223652</code>

После оплаты нажми кнопку ниже и пришли скрин платежа 🧾"""

THANK_YOU_TEXT = """Напиши мне пожалуйста сюда [👉 нажми](https://t.me/m/PESxpZW1NGMy) любое приветствие или смайлик, скоро мы проверим перевод и сразу вышлем тебе гайд в этот чат 🌱✨

Спасибо за доверие! Пусть он принесёт тебе много пользы, лёгкости и вдохновения на пути к вкусному и здоровому питанию 💚

Так же можешь подписаться на мой [телеграм канал](https://t.me/lilarisyet), там я буду делиться новыми интересными гайдами ❤️🔥"""

# ── Клавиатуры ─────────────────────────────────────────────────────────────────

def buy_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Купить — 7$", callback_data="buy")]
    ])

def paid_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Я оплатил(а)!", callback_data="oplatil")]
    ])

def payment_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ PayPal 💻 — международные переводы", callback_data="pay_paypal")],
        [InlineKeyboardButton("2️⃣ Украинская карта 🇺🇦", callback_data="pay_ukraine")],
        [InlineKeyboardButton("3️⃣ Грузинская карта 🇬🇪 — международные переводы", callback_data="pay_georgia")],
        [InlineKeyboardButton("4️⃣ Криптовалюта 💎 USDT TRC20", callback_data="pay_crypto")],
    ])

# ── Хендлеры ──────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(GUIDE_TEXT, reply_markup=buy_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.message.reply_text(PAYMENT_TEXT, reply_markup=payment_keyboard())

    elif query.data == "pay_paypal":
        await query.message.reply_html(PAYPAL_TEXT, reply_markup=paid_keyboard())

    elif query.data == "pay_ukraine":
        await query.message.reply_html(UKRAINE_TEXT, reply_markup=paid_keyboard())

    elif query.data == "pay_georgia":
        await query.message.reply_html(GEORGIA_TEXT, reply_markup=paid_keyboard())

    elif query.data == "pay_crypto":
        await query.message.reply_html(CRYPTO_TEXT, reply_markup=paid_keyboard())


    elif query.data == "oplatil":
        user = query.from_user
        username = f"@{user.username}" if user.username else f"ID: {user.id}"
        name = user.full_name
        await query.message.reply_text("📸 Пришли скрин платежа следующим сообщением!")
        try:
            await context.bot.send_message(
                chat_id=ADMIN_GROUP_ID,
                text=f"🔔 Новая оплата!\n\n👤 Покупатель: {name}\n📱 Аккаунт: {username}\n\nОжидай скрин следующим сообщением 👇"
            )
        except Exception as e:
            logger.warning(f"Не удалось отправить уведомление в группу: {e}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    username = f"@{user.username}" if user.username else f"ID: {user.id}"
    name = user.full_name
    # Отвечаем покупателю благодарственным сообщением
    await update.message.reply_markdown(THANK_YOU_TEXT)
    # Пересылаем скрин в группу
    try:
        await context.bot.send_message(
            chat_id=ADMIN_GROUP_ID,
            text=f"📸 Скрин оплаты от {name} ({username}):"
        )
        await context.bot.forward_message(
            chat_id=ADMIN_GROUP_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
    except Exception as e:
        logger.warning(f"Не удалось переслать скрин: {e}")

# ── Запуск ────────────────────────────────────────────────────────────────────

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    logger.info("Бот запущен!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
