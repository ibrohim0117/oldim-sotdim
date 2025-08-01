from aiogram import types, F, Router

from keyboards.defoults import category_menu, new_or_old



user_router = Router()

@user_router.message(F.text=='Sotib olaman 🚗')
async def sale_car(msg: types.Message):
    await msg.answer("Mashina kategoriyalari", reply_markup=new_or_old)
