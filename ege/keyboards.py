from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def default():
	btn1 = KeyboardButton(text='🍧 Поменять раздел')
	btn2 = KeyboardButton(text='Разделы 🍨')
	btn3 = KeyboardButton(text='🫐 Выполнено')
	btn4 = KeyboardButton(text='Вывести 🔮')
	kb = ReplyKeyboardMarkup(
		keyboard=[
			[btn1, btn2],
			[btn3, btn4]
		],
		resize_keyboard=True
		)
	return kb