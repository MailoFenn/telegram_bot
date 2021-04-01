import logging
import time
import os
import vk_api
import config


from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = config.API_TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def help_func(message: types.Message):
    user = message.from_user
    print(f'{user.username} {user.id}')
    if user.id == 368028746:
        time.sleep(2)
        await message.reply(text='Опять кринж...(')


if __name__ == '__main__':
    # vk_session = vk_api.VkApi('+79051152766', '12321C03086c')
    # vk_session.auth()
    # vk = vk_session.get_api()
    # vk_api.V
    executor.start_polling(dp, skip_updates=True)

