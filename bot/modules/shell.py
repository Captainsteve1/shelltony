from subprocess import run as srun
from telegram.ext import Filters, MessageHandler

from bot import dispatcher
from bot.utils.filters import CustomFilters
from bot.utils.message_utils import sendMessage


def shell(update, context):
    message = update.effective_message
    cmd = message.text
    process = srun(cmd, capture_output=True, shell=True)
    reply = ''
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')
    if len(stdout) != 0:
        reply += f"<b>Stdout</b>\n<code>{stdout}</code>\n"
    if len(stderr) != 0:
        reply += f"<b>Stderr</b>\n<code>{stderr}</code>\n"
    if len(reply) > 3000:
        with open('output.txt', 'w') as file:
            file.write(reply)
        with open('output.txt', 'rb') as doc:
            context.bot.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id)
    elif len(reply) != 0:
        sendMessage(reply, context.bot, update.message)
    else:
        sendMessage('Executed', context.bot, update.message)


SHELL_HANDLER = MessageHandler(filters = CustomFilters.sudo_user & Filters.regex(r'^(\w.*)$'), callback=shell, run_async=True)
dispatcher.add_handler(SHELL_HANDLER)