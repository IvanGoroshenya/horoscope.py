
from aiogram import Bot, Dispatcher, executor, types, filters
from config import TOKEN, text_1
from horoscope import aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardButton, InlineKeyboardMarkup
import random
from datetime import datetime
from config import card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, \
    card_12, card_13, card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



async def on_startup(_):
    print('Бот работает')


context = {}

urlkb = InlineKeyboardMarkup(row_width=2)

k1 = InlineKeyboardButton(text='Овен ♈', callback_data='aries')
k2 = InlineKeyboardButton(text='Телец ♉ ', callback_data='taurus')
k3 = InlineKeyboardButton(text='Близнецы ♊', callback_data='gemini')
k4 = InlineKeyboardButton(text='Рак ♋', callback_data='cancer')
k5 = InlineKeyboardButton(text='Лев ♌', callback_data='leo')
k6 = InlineKeyboardButton(text='Дева ♍', callback_data='virgo' )
k7 = InlineKeyboardButton(text='Весы ♎', callback_data='libra')
k8 = InlineKeyboardButton(text='Скорпион ♏', callback_data='scorpio')
k9 = InlineKeyboardButton(text='Стрелец ♐', callback_data='sagittarius')
k10 = InlineKeyboardButton(text='Козерог ♑', callback_data='capricorn')
k11 = InlineKeyboardButton(text='Водолей ♒', callback_data='aquarius')
k12 = InlineKeyboardButton(text='Рыбы ♓ ', callback_data='pisces')

urlkb.add(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12)

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/Taro')
b3 = KeyboardButton('/Horoscope')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3)



#########################################       Гороскоп                  ###############################################
@dp.message_handler(commands=['Horoscope'])
async def goroskop(message: types.Message):
    await message.answer(text='Выберите свой знак зодиака', reply_markup=urlkb)

@dp.callback_query_handler(text = 'aries')
async def zodiak_1(callback: types.CallbackQuery):
    await callback.message.reply(aries())


@dp.callback_query_handler(text = 'taurus')
async def zodiak_2(callback: types.CallbackQuery):
    await callback.message.reply(taurus())


@dp.callback_query_handler(text = 'gemini')
async def zodiak_3(callback: types.CallbackQuery):
    await callback.message.reply(gemini())


@dp.callback_query_handler(text = 'cancer')
async def zodiak_4(callback: types.CallbackQuery):
    await callback.message.reply(cancer())

@dp.callback_query_handler(text = 'leo')
async def zodiak_5(callback: types.CallbackQuery):
    await callback.message.reply(leo())

@dp.callback_query_handler(text = 'virgo')
async def zodiak_6(callback: types.CallbackQuery):
    await callback.message.reply(virgo())

@dp.callback_query_handler(text = 'libra')
async def zodiak_7(callback: types.CallbackQuery):
    await callback.message.reply(libra())

@dp.callback_query_handler(text = 'scorpio')
async def zodiak_8(callback: types.CallbackQuery):
    await callback.message.reply(scorpio())


@dp.callback_query_handler(text = 'sagittarius')
async def zodiak_9(callback: types.CallbackQuery):
    await callback.message.reply(sagittarius())


@dp.callback_query_handler(text = 'capricorn')
async def zodiak_10(callback: types.CallbackQuery):
    await callback.message.reply(capricorn())



@dp.callback_query_handler(text = 'aquarius')
async def zodiak_11(callback: types.CallbackQuery):
    await callback.message.reply(aquarius())



@dp.callback_query_handler(text = 'pisces')
async def zodiak_12(callback: types.CallbackQuery):
    await callback.message.reply(pisces())




#########################################################################################################################



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    with open('E:\Taro\img\witcher.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await bot.send_message(message.chat.id, text_1, reply_markup=kb_client)
    await bot.send_message(message.chat.id, 'Команды :\n'
                                            '/start\n'
                                            '/Taro\n'
                                            '/Horoscope')


@dp.message_handler(commands=['Taro'])
async def q(message: types.Message):
    last_command = context.get(message.chat.id)

    if not last_command or (datetime.now() - last_command).seconds > 21600:
        num = random.randint(1, 22)
        if num == 1:
            with open('E:\Taro\img\башня.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_1, reply_markup=kb_client)

        if num == 2:
            with open('E:\Taro\img\верховная_жрица.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_2, reply_markup=kb_client)
        if num == 3:
            with open('E:\Taro\img\верховный_жрец.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_3, reply_markup=kb_client)
        if num == 4:
            with open('E:\Taro\img\дьявол.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_4, reply_markup=kb_client)
        if num == 5:
            with open('E:\Taro\img\звезда.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_5, reply_markup=kb_client)
        if num == 7:
            with open('E:\Taro\img\император.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_6, reply_markup=kb_client)
        if num == 6:
            with open('E:\Taro\img\императрица.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_7, reply_markup=kb_client)
        if num == 8:
            with open('E:\Taro\img\колесница.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_8, reply_markup=kb_client)
        if num == 9:
            with open('E:\Taro\img\колесо_судьбы.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_9, reply_markup=kb_client)
        if num == 10:
            with open('E:\Taro\img\луна.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_10, reply_markup=kb_client)
        if num == 11:
            with open('E:\Taro\img\любовники.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_11, reply_markup=kb_client)
        if num == 12:
            with open('E:\Taro\img\маг.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_12, reply_markup=kb_client)
        if num == 13:
            with open('E:\Taro\img\мир.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_13, reply_markup=kb_client)
        if num == 14:
            with open('E:\Taro\img\отшельник.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_14, reply_markup=kb_client)
        if num == 15:
            with open('E:\Taro\img\повешенный.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_15, reply_markup=kb_client)
        if num == 16:
            with open('E:\Taro\img\сила.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_16, reply_markup=kb_client)
        if num == 17:
            with open('E:\Taro\img\смерть.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_17, reply_markup=kb_client)
        if num == 18:
            with open('E:\Taro\img\солнце.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_18, reply_markup=kb_client)
        if num == 19:
            with open('E:\Taro\img\справедливость.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_19, reply_markup=kb_client)
        if num == 20:
            with open('E:\Taro\img\суд.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_20, reply_markup=kb_client)
        if num == 21:
            with open('E:\Taro\img\умеренность.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_21, reply_markup=kb_client)
        if num == 22:
            with open('E:\Taro\img\шут.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=card_22, reply_markup=kb_client)

        context[message.chat.id] = datetime.now()
    else:
        await message.reply('Повторите попытку позже, ваша карта на сегодня получена (｡◕‿‿◕｡)')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
