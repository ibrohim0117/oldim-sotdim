import logging
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from environs import Env

from middlewares.i18n import i18n_middleware
from aiogram_i18n.context import I18nContext
from keyboards.defoults import main_menu, category_menu, new_or_old

from handlers.users import user_router
from handlers.channel import nimadur_router
from handlers.utiltiy import utiltiy_router
from handlers.sell import sell_router

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

API_TOKEN = env.str("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

i18n_middleware.setup(dispatcher=dp)


@dp.message(Command("start"))
async def send_welcome(message: types.Message, i18n: I18nContext):
    await i18n.set_locale(message.from_user.language_code)
    await message.answer(i18n("start_text"), reply_markup=main_menu(i18n))



async def main():
    dp.include_router(user_router)
    dp.include_router(nimadur_router)
    dp.include_router(utiltiy_router)
    dp.include_router(sell_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())