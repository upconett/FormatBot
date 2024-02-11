import asyncio
from create_bot import bot, dp
from ege.handlers import router


async def on_startup():
	print("'K, let's do some formatting!\n")


async def on_shutdown():
	print("\nSee you later!")


async def main():
	dp.startup.register(on_startup)
	dp.shutdown.register(on_shutdown)
	dp.include_router(router)

	await bot.delete_webhook(drop_pending_updates = True)
	await dp.start_polling(bot)


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		pass