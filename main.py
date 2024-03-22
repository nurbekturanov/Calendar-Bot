from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from telegram import Update
from calendar_handler import main_handler, calendar_handler, callback_query_handler
import settings


def main() -> None:
    app = Application.builder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("calendar", calendar_handler))
    app.add_handler(MessageHandler(filters.ALL, main_handler))
    app.add_handler(CallbackQueryHandler(callback_query_handler))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
