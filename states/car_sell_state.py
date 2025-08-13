from aiogram.fsm.state import State, StatesGroup


class CarSellSate(StatesGroup):
    hajmi = State()
    brand = State()
    region = State()
    pay = State()
    price = State()
    year = State()
    image = State()
    phone = State()
    about = State()