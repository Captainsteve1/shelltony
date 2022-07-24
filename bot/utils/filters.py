from telegram.ext import MessageFilter
from telegram import Message
from bot import SUDO_USERS, OWNER_ID


class CustomFilters:
    class __OwnerFilter(MessageFilter):
        def filter(self, message: Message):
            return message.from_user.id == OWNER_ID

    owner_filter = __OwnerFilter()

    class __SudoUser(MessageFilter):
        def filter(self, message: Message):
            return message.from_user.id in SUDO_USERS or message.from_user.id == OWNER_ID

    sudo_user = __SudoUser()

    def _owner_query(self):
        return self == OWNER_ID or self in SUDO_USERS