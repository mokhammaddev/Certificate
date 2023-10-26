import asyncio
import sys

import cv2
from aiogram import F, Router
from PIL import Image
from aiogram.types import *
from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher
from io import BytesIO
from markup import *
from inline import *


from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5997549250:AAHIwR6lVFzdoIqs7v5zUubOvS4mHzV8-RU")


async def start(message: Message):
    img = FSInputFile("Certificate-shablon/certificate.png")
    await message.answer(
        f"Assalomu alekum {message.from_user.full_name} Sertifikat tayyorlaydigan botga xush kelibsiz!"
        f"Bu bot orqali o’zingizga sertifikat tayyorlab olishingiz mumkin.")
    await message.answer_photo(img, caption="Marhamat quyidagi sertifikatni o’zingizga moslab o’zgartiring/n"
                                            "Pastdagi inlinelar orqali ketma-ket amallarni bajarishingiz mukin",
                               reply_markup=bosh_kb)


async def one(message: Message):
    img = FSInputFile("Certificate-shablon/certificate-1.png")
    await message.answer_photo(img, caption="Boshladik")
    await message.answer("1-bosqich Bo'sh o'ringga yozuv yozing!")


async def one_message(message: Message):
    template = cv2.imread('Certificate-shablon/certificat_bosh.png')
    if 15 > len(message.text) >= 3:
        if 6 >= len(message.text) >= 3:
            cv2.putText(template, message.text, (230, 51), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        elif 12 > len(message.text) > 6:
            cv2.putText(template, message.text, (215, 51), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        elif 15 >= len(message.text) >= 12:
            cv2.putText(template, message.text, (200, 51), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg", template)
        img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
        await message.answer_photo(img)
        await message.answer("1-bosqich tugadi davom ettiring!", reply_markup=one_line)
    elif len(message.text) < 3:
        await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
    elif len(message.text) > 15:
        await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")


async def two(call: CallbackQuery):
    img = FSInputFile("Certificate-shablon/certificate-2.png")
    await bot.send_photo(chat_id=call.message.chat.id, photo=img)
    await call.message.answer("2-bosqich Bo'sh o'ringga yozuv yozing!")


async def two_message(message: Message):
    template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
    if 15 > len(message.text) >= 3:
        if 6 >= len(message.text) >= 3:
            cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        elif 12 > len(message.text) > 6:
            cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        elif 15 >= len(message.text) >= 12:
            cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg", template)
        img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
        await message.answer_photo(img)
        await message.answer("2-bosqich tugadi davom ettiring!", reply_markup=two_line)
    elif len(message.text) < 3:
        await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
    elif len(message.text) > 15:
        await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")


dp = Dispatcher()

dp.message.register(start, F.text == '/start')
dp.message.register(one, F.text == "Boshlash💥")
dp.message.register(one_message)
dp.callback_query.register(two, F.data.startswith("two_line"))
dp.message.register(two_message)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
