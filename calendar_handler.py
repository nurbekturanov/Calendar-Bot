from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from keyboards import generate_month_keyboard, generate_year_keyboard
import datetime


async def calendar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = generate_month_keyboard(None)

    await update.message.reply_text(
        "Here is it!", reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data.startswith("date"):
        _, month, year = data.split("|")
        new_date = datetime.date(int(year), int(month), 1)
        keyboard = generate_month_keyboard(new_date)
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
    elif data.startswith("year"):
        _, year = data.split("|")
        keyboard = generate_year_keyboard(int(year))
        await context.bot.edit_message_reply_markup(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


async def main_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("/calendar")]], resize_keyboard=True
        ),
    )
