from config import TOKEN
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler, Filters, CallbackContext
import bot


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    #Bot commands
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("help", bot.help_command))
    dispatcher.add_handler(CommandHandler("Parte1", bot.parte1))
    dispatcher.add_handler(CommandHandler("Parte2", bot.parte2))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot.echo))

    #Run and start bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()