import requests
from aiogram import types
import time


class Request:

    def __init__(self, url, bot, chat_id):
        self.count = 0
        self.url = url
        self.bot = bot
        self.chat_id = chat_id

    async def start(self):
        while True:
            response = requests.post(self.url)
            count_new = response.json()['response']['count']
            if self.count == 0:
                self.count = count_new
                post = response.json()['response']['items'][0]
                await self.send_new_post(post=post)
            elif count_new > self.count:
                for num in range(count_new-self.count):
                    post = response.json()['response']['items'][num]
                    await self.send_new_post(post=post)
                self.count = count_new
            time.sleep(5)

    async def send_new_post(self, post):
        photo_quantity = len(post['attachments'])
        if photo_quantity > 1 and post['attachments'][0]['type'] == 'photo':
            await self.send_photos(post=post, photo_quantity=photo_quantity)
            await self.send_text(post=post)
        elif photo_quantity == 1 and post['attachments'][0]['type'] == 'photo':
            await self.send_photo(post=post)
        else:
            await self.send_text(post=post)

    async def send_photo(self, post):
        photo = post['attachments'][0]['photo']['sizes']
        photo_url = ''
        for item in photo:
            if item['type'] == 'z':
                photo_url = str(item['url'])
        await self.bot.send_photo(chat_id=self.chat_id,
                                  photo=photo_url,
                                  caption=post['text'])

    async def send_text(self, post):
        await self.bot.send_message(chat_id=self.chat_id,
                                    text=post['text'])

    async def send_photos(self, post, photo_quantity):
        photo_arr = types.MediaGroup()
        for num in range(photo_quantity):
            for photo in post['attachments'][num]['photo']['sizes']:
                if photo['type'] == 'z':
                    photo_tmp = types.InputMediaPhoto(
                        media=str(photo['url']))
                    photo_arr.attach_photo(photo_tmp)
        await self.bot.send_media_group(chat_id=self.chat_id,
                                            media=photo_arr)
