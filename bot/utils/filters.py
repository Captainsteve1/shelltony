from telegram import Message
from telegram.ext import MessageFilter

from bot import AUTHORIZED_CHATS, OWNER_ID

class CustomFilters:
    class __OwnerFilter(MessageFilter):
        def filter(self, message: Message):
            return message.from_user.id == OWNER_ID

    owner_filter = __OwnerFilter()

    class __AuthorizedUserFilter(MessageFilter):
        def filter(self, message: Message):
            id = message.from_user.id
            return bool(id in AUTHORIZED_CHATS or id == OWNER_ID)

    authorized_user = __AuthorizedUserFilter()

    class __AuthorizedChat(MessageFilter):
        def filter(self, message: Message):
            return bool(message.chat.id in AUTHORIZED_CHATS)

    authorized_chat = __AuthorizedChat()

    class __SudoUser(MessageFilter):
        def filter(self, message: Message):
            return message.from_user.id in SUDO_USERS or message.from_user.id == OWNER_ID

    sudo_user = __SudoUser()

    def _owner_query(self):
        return self == OWNER_ID or self in SUDO_USERS
