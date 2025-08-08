from aiogram import types, F, Router
from aiogram_i18n.context import I18nContext

from keyboards.defoults import mashina_tipi, category_menu, region_menu




sell_router = Router()

@sell_router.message(lambda message, i18n: message.text == i18n("sell_button"))
async def sell_car(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("car_categories"), reply_markup=mashina_tipi(i18n))



@sell_router.message(lambda message, i18n: message.text == i18n("car_light_button"))
async def car_yengil(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("car_categories"), reply_markup=category_menu)


@sell_router.message(lambda message, i18n: message.text == i18n("car_heavy_button"))
async def car_ogir(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("car_categories"), reply_markup=category_menu)



@sell_router.message(F.text == "BMW")
async def car_bmw(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("region_list"), reply_markup=region_menu(i18n))

