import asyncio
import logging

from Request import Request
import config
import urls

from aiogram import Bot, Dispatcher, executor, types

TELEGRAM_TOKEN = config.TELEGRAM_TOKEN
VK_TOKEN = config.VK_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def help_func(message: types.Message):
    mf = Request(url=urls.MF, bot=bot, chat_id=message.from_user.id)
    print(message.from_user.id)

    await mf.start()


@dp.message_handler(commands='start2')
async def help_func(message: types.Message):
    bw = Request(url=urls.BW, bot=bot, chat_id=message.from_user.id)

    await bw.start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
