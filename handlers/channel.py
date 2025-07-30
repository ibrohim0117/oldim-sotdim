from aiogram import types, Router, F
from keyboards.defoults import category_menu



nimadur_router = Router()

@nimadur_router.message(F.text=='salom')
async def aa(msg: types.Message):
    await msg.answer("Nimadur ishladi!")