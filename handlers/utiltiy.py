from aiogram import types, F, Router
from aiogram_i18n.context import I18nContext
from keyboards.defoults import language_button, main_menu



utiltiy_router = Router()

@utiltiy_router.message(lambda message, i18n: message.text == i18n("language_button"))
async def change_language(msg: types.Message, i18n: I18nContext):
    await msg.answer(i18n("language"), reply_markup=language_button(i18n))


@utiltiy_router.message(lambda message, i18n: message.text == i18n("lang_uz_button"))
async def l_uz(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('uz')
    await msg.answer(i18n("language_select"), reply_markup=main_menu(i18n))

@utiltiy_router.message(lambda message, i18n: message.text == i18n("lang_ru_button"))
async def l_ru(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('ru')
    await msg.answer(i18n("language_select"), reply_markup=main_menu(i18n))

@utiltiy_router.message(lambda message, i18n: message.text == i18n("lang_en_button"))
async def l_en(msg: types.Message, i18n: I18nContext):
    await i18n.set_locale('en')
    await msg.answer(i18n("language_select"), reply_markup=main_menu(i18n))