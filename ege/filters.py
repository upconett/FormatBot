from aiogram.filters import BaseFilter
from aiogram.types import Message
from create_bot import ownerId


class IndentFilter(BaseFilter):
	async def __call__(self, message: Message):
		try:
			lines = message.text.split('\n')
		except:
			try:
				lines = message.caption.split('\n')
			except:
				lines = ''
		try:
			int(lines[0])
		except:
			return False
		if len(lines) < 2:
			return False
		return True


class IsOwner(BaseFilter):
	async def __call__(self, message: Message):
		print(ownerId, message.from_user.id)
		return message.from_user.id == ownerId