from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext


def language_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('lang_uz_button')),
                KeyboardButton(text=_('lang_ru_button')),
                KeyboardButton(text=_('lang_en_button')),
            ]
        ],
        resize_keyboard=True
    )



def main_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('buy_button')),
                KeyboardButton(text=_('sell_button'))
            ],
            [
                KeyboardButton(text=_('my_ads_button'))
            ],
            [
                KeyboardButton(text=_('language_button')),
                KeyboardButton(text=_('contact_button'))
            ]
        ],
        resize_keyboard=True
    )


def mashina_tipi(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n  
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('car_light_button')),
                KeyboardButton(text=_('car_heavy_button'))
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


year_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='2030 - 2025'),
            KeyboardButton(text='2025 - 2020'),
            KeyboardButton(text="2020 - 2015")
        ],
        [
            KeyboardButton(text='2015 - 2010'),
            KeyboardButton(text='2010 - 2005')
        ],
        [
            KeyboardButton(text='2005 - 2000'),
            KeyboardButton(text='2000 - 19...')
        ]
    ],
    resize_keyboard=True
)

def region_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n  # tarjima funksiyasi

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('tashkent_button')),
                KeyboardButton(text=_('samarkand_button'))
            ],
            [
                KeyboardButton(text=_('fergana_button')),
                KeyboardButton(text=_('andijan_button'))
            ],
            [
                KeyboardButton(text=_('namangan_button')),
                KeyboardButton(text=_('bukhara_button'))
            ],
            [
                KeyboardButton(text=_('navoi_button')),
                KeyboardButton(text=_('jizzakh_button'))
            ],
            [
                KeyboardButton(text=_('syrdarya_button')),
                KeyboardButton(text=_('surkhandarya_button'))
            ],
            [
                KeyboardButton(text=_('kashkadarya_button')),
                KeyboardButton(text=_('khorezm_button'))
            ],
            [
                KeyboardButton(text=_('karakalpakstan_button'))
            ]
        ],
        resize_keyboard=True
    )


def mashina_tulovi(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n  
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('nasiya')),
                KeyboardButton(text=_('naqt')),
                KeyboardButton(text='bank')
            ]
        ],
        resize_keyboard=True
    )


def mashina_holati(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n  
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('yangi')),
                KeyboardButton(text=_('urtacha')),
                KeyboardButton(text='eski')
            ]
        ],
        resize_keyboard=True
    )


def send_contact(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_('send_phone'), request_contact=True)]
        ],
        resize_keyboard=True
    )


