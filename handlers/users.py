from aiogram import types, F, Router

from keyboards.defoults import category_menu



user_router = Router()

@user_router.message(F.text=='Sotib olaman 🚗')
async def sale_car(msg: types.Message):
    await msg.answer("Mashina kategoriyalari")
