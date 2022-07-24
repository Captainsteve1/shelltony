from time import time
from bot import updater, LOGGER, dispatcher
from bot.utils.filters import CustomFilters
from telegram.ext import Filters, MessageHandler
from bot.utils.message_utils import editMessage, sendLogFile, sendMessage
from .modules import shell, authorize, leech_settings

def ping(update, context):
    start_time = int(round(time() * 1000))
    reply = sendMessage("Starting Ping", context.bot, update.message)
    end_time = int(round(time() * 1000))
    editMessage(f'{end_time - start_time} ms', reply)

def help(update, context):
    mes = "<b>Commands</b>:\n" + "<code>!p</code> - Ping\n"
    mes += "<code>!log</code> - Logs\n"
    mes += "<code>!help</code> - Help\n"
    mes += "<b>Example</b> : - <code>ffmpeg -version</code>\n"
    return sendMessage(mes, context.bot, update.message)

def log(update, context):
    sendLogFile(context.bot, update.message)

def main():
    ping_handler = MessageHandler(filters = CustomFilters.sudo_user & Filters.regex(r'(!p|!P)$'), callback=ping, run_async=True)
    log_handler = MessageHandler(filters=CustomFilters.sudo_user & Filters.regex(r'(!log|!LOG)$'), callback=log, run_async=True)
    help_handler = MessageHandler(filters=CustomFilters.sudo_user & Filters.regex(r'(!help|!HELP)$'), callback=help, run_async=True)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(log_handler)
    dispatcher.add_handler(help_handler)
    updater.start_polling(drop_pending_updates = True)
    LOGGER.info("Bot Started!")
