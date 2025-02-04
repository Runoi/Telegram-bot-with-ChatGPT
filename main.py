import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from chatgpt import ask

# Загружаем переменные из .env
load_dotenv('key.env')
bot_key = os.getenv('TELEGRAM_BOT_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=bot_key)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, интегрированный с ChatGPT. Отправь мне сообщение, и я отвечу.")

@dp.message(Command('help'))
async def send_welcome(message: types.Message):
    await message.reply("Я бот, интегрированный с ChatGPT. Моя тематика/специализация История России.\n\nМеня обучали на базе знаний с 3152 строками\n\n Я понимаю запросы как на русском, так и на английском, например: Кратко расскажи об истории России. PS Язык ответа зависит от языка вопроса")

# Обработчик текстовых сообщений
@dp.message()
async def echo(message: types.Message):
    # Отправляем сообщение пользователя в ChatGPT
    response = ask(message.text)

    # Отправляем ответ пользователю
    await message.answer(response)


async def main():
    await dp.start_polling(bot)

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())

