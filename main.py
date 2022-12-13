import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5810144831:AAEwy32UfUIdq8oF0gW4-LFwYUvSq3uOGKs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("Bu bot sizga foydali malumotlarni ulashadi")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Salom botga xush kelibsiz!")

wikipedia.set_lang('uz')
@dp.message_handler()
async def echo(message: types.Message):
    matn = message.text
    try:
        javob = wikipedia.summary(matn)
        await message.reply(javob)
    except:
        await message.reply('bu mavzuga oid maqola topilmadi!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
