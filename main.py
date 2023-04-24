from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6157596715:AAFaJ0TdMj2AbdOkENUymVmKAdaxmHzSIBU')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Web Page', web_app=WebAppInfo(url= 'https://mirl1x.github.io/test5/')))
    await message.answer('Hello world! Please! Press the button on the Keyboard ', reply_markup=markup)

executor.start_polling(dp)

