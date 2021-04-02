import logging
import time
from pprint import pprint

from Request import Request
import requests
import config
import urls

from aiogram import Bot, Dispatcher, executor, types

TELEGRAM_TOKEN = config.TELEGRAM_TOKEN
VK_TOKEN = config.VK_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
# count = 0


# async def send_photos(post, chat_id):
#     photo_arr = types.MediaGroup()
#     for photo in post['attachments']:
#         photo = photo['photo']['sizes']
#         for item in photo:
#             if item['type'] == 'z':
#                 photo_tmp = types.InputMediaPhoto(
#                     media=str(item['url']))
#                 photo_arr.attach_photo(photo_tmp)
#     await bot.send_media_group(chat_id=chat_id, media=photo_arr)
#
#
# async def send_text(post, chat_id):
#     await bot.send_message(chat_id=chat_id, text=post['text'])
#
#
# async def send_photo(post, chat_id):
#     photo = post['attachments']['photo']['sizes']
#     photo_url = ''
#     for item in photo:
#         if item['type'] == 'z':
#             photo_url = str(item['url'])
#     await bot.send_photo(chat_id=chat_id, photo=photo_url,
#                          caption=post['text'])
#
#
# async def send_new_post(post, chat_id):
#     if len(post['attachments']) > 0:
#         await send_photos(chat_id=chat_id, post=post)
#         await send_text(chat_id=chat_id, post=post)
#     elif len(post['attachments']) > 1:
#         await send_photo(chat_id=chat_id, post=post)
#     else:
#         await send_text(chat_id=chat_id, post=post)


# @dp.message_handler(commands='start')
# async def help_func(message: types.Message):
#     global count
#     chat_id = message.from_user.id
#     while True:
#         response = requests.post(f'https://api.vk.com/method/'
#                                  f'wall.get?owner_id=-43275378&query="date=1617194081"'
#                                  f'&access_token={VK_TOKEN}&v=5.130')
#         response2 = requests.post(f'https://api.vk.com/method/'
#                                  f'wall.get?owner_id=-601624&query="date=1617194081"'
#                                  f'&access_token={VK_TOKEN}&v=5.130')
#         count_new = response.json()['response']['count']
#         if count == 0:
#             count = count_new
#             post = response.json()['response']['items'][0]
#             await send_new_post(post=post, chat_id=chat_id)
#         elif count_new > count:
#             for num in range(count_new-count):
#                 post = response.json()['response']['items'][num]
#                 await send_new_post(post=post, chat_id=chat_id)
#             count = count_new
#         time.sleep(5)

@dp.message_handler(commands='start')
async def help_func(message: types.Message):
    mf = Request(url=urls.BW, bot=bot, chat_id=message.from_user.id)
    await mf.start()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


