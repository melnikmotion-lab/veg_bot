import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
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

# Карусель с описанием гайда, отправляется при /start
IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
GUIDE_IMAGES = [os.path.join(IMAGES_DIR, f"{i:02d}.jpg") for i in range(1, 9)]

PAYMENT_TEXT = "Какой способ оплаты вам удобен? 💳✨"

PAYPAL_TEXT = """💻 <b>Оплата через PayPal</b>

Переведи 7$ на:
📧 <code>jagannathastaka108@gmail.com</code>

После оплаты нажми кнопку ниже и пришли скрин платежа 🧾"""

UKRAINE_TEXT = """🇺🇦 <b>Украинская карта</b>

• Номер карты: <code>4441111046345736</code>
• Получатель: Мельнік Ліла

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

RUSSIA_TEXT = """🇷🇺 <b>Оплата с российской карты</b>

С российской карты можно отправить перевод на мою грузинскую карту через сервис <b>Korona Pay</b> (Золотая Корона) — на сайте koronapay.com или в их приложении.

Выбери перевод в Грузию по номеру карты и переведи сумму, эквивалентную 7$ 👇

🇬🇪 <b>Грузинская карта (Bank of Georgia)</b>
• Номер карты: <code>5488880047494286</code>
• Получатель: MELNIK OLEKSII

После оплаты нажми кнопку ниже и пришли скрин платежа 🧾"""

THANK_YOU_TEXT = """Напиши мне пожалуйста сюда [👉 нажми](https://t.me/m/PESxpZW1NGMy) любое приветствие или смайлик, скоро мы проверим перевод и сразу вышлем тебе гайд в этот чат 🌱✨

Спасибо за доверие! Пусть он принесёт тебе много пользы, лёгкости и вдохновения на пути к вкусному и здоровому питанию 💚

Так же можешь подписаться на мой [телеграм канал](https://t.me/lilarisyet), там я буду делиться новыми интересными гайдами ❤️🔥"""

# ── Клавиатуры ─────────────────────────────────────────────────────────────────

def paid_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Я оплатил(а)!", callback_data="oplatil")]
    ])

def payment_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Российская карта 🇷🇺", callback_data="pay_russia")],
        [InlineKeyboardButton("2️⃣ Украинская карта 🇺🇦", callback_data="pay_ukraine")],
        [InlineKeyboardButton("3️⃣ PayPal 💻 — международные переводы", callback_data="pay_paypal")],
        [InlineKeyboardButton("4️⃣ Грузинская карта 🇬🇪 — международные переводы", callback_data="pay_georgia")],
        [InlineKeyboardButton("5️⃣ Криптовалюта 💎 USDT TRC20", callback_data="pay_crypto")],
    ])

# ── Хендлеры ──────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    media = []
    for path in GUIDE_IMAGES:
        with open(path, "rb") as f:
            media.append(InputMediaPhoto(f.read()))
    await update.message.reply_media_group(media)
    await update.message.reply_text(PAYMENT_TEXT, reply_markup=payment_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.message.reply_text(PAYMENT_TEXT, reply_markup=payment_keyboard())

    elif query.data == "pay_paypal":
        await query.message.reply_html(PAYPAL_TEXT, reply_markup=paid_keyboard())

    elif query.data == "pay_ukraine":
        await query.message.reply_html(UKRAINE_TEXT, reply_markup=paid_keyboard())

    elif query.data == "pay_russia":
        await query.message.reply_html(RUSSIA_TEXT, reply_markup=paid_keyboard())

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
