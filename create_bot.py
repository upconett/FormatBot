from aiogram import Bot, Dispatcher

TOKEN = open('token.txt').readline()

bot = Bot(token = TOKEN, parse_mode='HTML')
dp = Dispatcher()
