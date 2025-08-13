from aiogram import types, F, Router
from aiogram_i18n.context import I18nContext

from keyboards.defoults import mashina_tipi, category_menu, region_menu, mashina_tulovi, year_menyu, mashina_holati
from aiogram.fsm.context import FSMContext

from states.car_sell_state import CarSellSate




sell_router = Router()

@sell_router.message(lambda message, i18n: message.text == i18n("sell_button"))
async def sell_car(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.set_state(CarSellSate.hajmi)
    await msg.answer(i18n("car_categories"), reply_markup=mashina_tipi(i18n))
    

@sell_router.message(CarSellSate.hajmi)
async def car_yengil(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(moshina_hajmi=msg.text)
    await msg.answer(text='Markani tanlang!', reply_markup=category_menu)
    await state.set_state(CarSellSate.brand)

@sell_router.message(CarSellSate.brand)
async def car_brand(msg: types.Message, i18n: I18nContext, state: FSMContext):
    await state.update_data(mashina_brand=msg.text)
    await msg.answer("Region", reply_markup=region_menu(i18n))
    await state.set_state(CarSellSate.region)


@sell_router.message(CarSellSate.region)
async def car_region(msg: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(car_region=msg.text)
    await msg.answer("To'lash", reply_markup=mashina_tulovi(i18n))
    await state.set_state(CarSellSate.pay)


@sell_router.message(CarSellSate.pay)
async def car_pay(msg: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(car_pay=msg.text)
    await msg.answer("Narxini kiriting ($ da yozing!)")
    await state.set_state(CarSellSate.price)


@sell_router.message(CarSellSate.price)
async def car_price(msg: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(car_price=msg.text)
    await msg.answer("Mashina ishlab chiqarilgan yil oralig'ini tanlang", reply_markup=year_menyu)
    await state.set_state(CarSellSate.year)


@sell_router.message(CarSellSate.year)
async def car_year(msg: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(car_year=msg.text)
    await msg.answer("Mashina rasmini yuboring", reply_markup=year_menyu)
    await state.set_state(CarSellSate.image)


@sell_router.message(CarSellSate.image, F.photo)
async def car_image(msg: types.Message, state: FSMContext, i18n: I18nContext):
    image_data = msg.photo[-1].file_id
    await state.update_data(car_image=image_data)
    await state.set_state(CarSellSate.phone)


@sell_router.message(CarSellSate.phone)
async def car_phone(msg: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(car_phone=msg.text)
    await msg.answer('Mashina haqida')
    await state.set_state(CarSellSate.about)


@sell_router.message(CarSellSate.about)
async def car_about(msg: types.Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(car_about=msg.text)
    data = await state.get_data()
    await msg.answer(
        f"✅ Elon qabul qilindi\n"
        f"Mashina hajmi: {data['moshina_hajmi']}\n"
        f"Mashina brandi: {data['mashina_brand']}\n"
        f"Mashina qayerda: {data['car_region']}\n"
        f"Mashina to'lovi: {data['car_pay']}\n"
        f"Mashina narxi: {data['car_price']}\n"
        f"Mashina yili: {data['car_year']}\n"
        f"Mashina rasmi: {data['car_image']}\n"
        f"Mashina holati: {data['car_position']}\n"
        f"Mashina egasi raqami: {data['car_phone']}\n"
        f"Mashina haqida qisqacha: {data['car_about']}\n"
       
    )
    await state.clear()










