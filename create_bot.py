from aiogram import Bot, Dispatcher
import os

TOKEN = open('token.txt').readline().replace('\n','').replace(' ','')
if not os.path.isdir('files'):
	os.makedirs('files')

bot = Bot(token = TOKEN, parse_mode='HTML')
dp = Dispatcher()
ownerId = int(open('owner.txt').readline())
