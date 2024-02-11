from aiogram import Bot, Dispatcher

TOKEN = open('token.txt').readline().replace('\n','').replace(' ','')
print(TOKEN)

bot = Bot(token = TOKEN, parse_mode='HTML')
dp = Dispatcher()
