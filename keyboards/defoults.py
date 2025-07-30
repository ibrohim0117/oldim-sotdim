from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sotib olaman 🚗'),
            KeyboardButton(text='Sotaman ＄')
        ],
        [
            KeyboardButton(text="Mening elonlarim ✉️")
        ],
        [
            KeyboardButton(text='Til (uz/ru/en) 🇺🇿'),
            KeyboardButton(text='Biz bilan aloqa 📞')
        ]
    ],
    resize_keyboard=True
)


category_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='BMW'),
            KeyboardButton(text='MERS'),
            KeyboardButton(text="AUDI")
        ],
        [
            KeyboardButton(text='OPEL'),
            KeyboardButton(text='TESLA')
        ],
        [
            KeyboardButton(text='BYD'),
            KeyboardButton(text='LADA'),
            KeyboardButton(text="GM") 
        ]
    ],
    resize_keyboard=True
)