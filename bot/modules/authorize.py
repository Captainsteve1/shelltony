from bot import SUDO_USERS, dispatcher
from bot.utils.message_utils import sendMessage
from telegram.ext import CommandHandler
from bot.utils.filters import CustomFilters

def addSudo(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in SUDO_USERS:
            msg = 'Already Sudo!'
        else:
            SUDO_USERS.add(user_id)
            msg = 'Promoted as Sudo'
    elif reply_message is None:
        msg = "Give ID or Reply To message of whom you want to Promote."
    else:
        # Trying to authorize someone by replying
        user_id = reply_message.from_user.id
        if user_id in SUDO_USERS:
            msg = 'Already Sudo!'
        else:
            SUDO_USERS.add(user_id)
            msg = 'Promoted as Sudo'
    sendMessage(msg, context.bot, update.message)

def removeSudo(update, context):
    reply_message = None
    message_ = None
    reply_message = update.message.reply_to_message
    message_ = update.message.text.split(' ')
    if len(message_) == 2:
        user_id = int(message_[1])
        if user_id in SUDO_USERS:
            msg = 'Demoted'
            SUDO_USERS.remove(user_id)
        else:
            msg = 'Not sudo user to demote!'
    elif reply_message is None:
        msg = "Give ID or Reply To message of whom you want to remove from Sudo"
    else:
        user_id = reply_message.from_user.id
        if user_id in SUDO_USERS:
            msg = 'Demoted'
            SUDO_USERS.remove(user_id)
        else:
            msg = 'Not sudo user to demote!'
    sendMessage(msg, context.bot, update.message)

def sendAuthChats(update, context):
    sudo = '' + '\n'.join(f"<code>{uid}</code>" for uid in SUDO_USERS)
    sendMessage(f'<b><u>Sudo Users:</u></b>\n{sudo}', context.bot, update.message)


send_auth_handler = CommandHandler(command='users', callback=sendAuthChats,
                                    filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)

addsudo_handler = CommandHandler(command='addsudo', callback=addSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)
removesudo_handler = CommandHandler(command='rmsudo', callback=removeSudo,
                                    filters=CustomFilters.owner_filter, run_async=True)

dispatcher.add_handler(send_auth_handler)
dispatcher.add_handler(addsudo_handler)
dispatcher.add_handler(removesudo_handler)
