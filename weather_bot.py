import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_API, APIKEY
from forecast import get_weather

# Bot object
bot = Bot(TELEGRAM_API)
# Dispatcher object
disp = Dispatcher(bot)
# Loger config
logging.basicConfig(level=logging.INFO)


# Handler for /start command
@disp.message_handler(commands="start")
async def bot_start(message: types.Message):
    await message.reply("Hello! I am a WeatherBot!\n"
                        "Type a city name")


@disp.message_handler()
async def get_observation(message: types.Message):
    weather = get_weather(str(message.text), APIKEY)
    forecast = ''
    for key, values in weather.items():
        forecast += f"{key}: {values}\n"
    await message.answer(forecast)


if __name__ == "__main__":
    executor.start_polling(disp, skip_updates=True)
