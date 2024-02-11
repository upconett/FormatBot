from aiogram.filters import BaseFilter
from aiogram.types import Message


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