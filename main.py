import logging
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# from middlewares.i18n import i18n_middleware
# from aiogram_i18n.context import I18nContext
API_TOKEN = env.str("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# i18n_middleware.setup(dispatcher=dp)


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Salom hammaga")
    # await message.answer(i18n.gettext("start_text"), reply_markup=main_menu)

@dp.message(F.text == 'nima')
async def nima(message: types.Message):
    await message.answer("Qovun")





async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())