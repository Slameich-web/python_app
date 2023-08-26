from aiogram import Bot, Dispatcher, executor
from bot_app.env import API_KEY

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)