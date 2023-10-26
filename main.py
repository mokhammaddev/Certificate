import asyncio
import cv2
from aiogram import F, Router
from PIL import Image
from aiogram.types import *
from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher
from io import BytesIO
from markup import bosh_kb
from inline import integer_kb

from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5997549250:AAHIwR6lVFzdoIqs7v5zUubOvS4mHzV8-RU")

dp = Dispatcher()


@dp.message(F.text == '/start')
async def start(message: Message):
    img = FSInputFile("certificate.png")
    await message.answer(
        f"Assalomu alekum {message.from_user.full_name} Sertifikat tayyorlaydigan botga xush kelibsiz!"
        f"Bu bot orqali o’zingizga sertifikat tayyorlab olishingiz mumkin.")
    await message.answer_photo(img, caption="Marhamat quyidagi sertifikatni o’zingizga moslab o’zgartiring/n"
                                            "Pastdagi inlinelar orqali ketma-ket amallarni bajarishingiz mukin",
                               reply_markup=bosh_kb)


@dp.message(F.text == "Start💥")
async def one(message: Message):
    img = FSInputFile("certificate-1.png")
    await message.answer_photo(img, caption="Bo'sh o'ringga yozuv yozing!")


# @dp.message()
# async def one_message(message: Message):
#     template = cv2.imread('certificate-1.png')
#     cv2.putText(template, message.text, (277, 111), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
#     cv2.imwrite(f"C:/Users/Muhammad/Desktop/Sinov-Proyekt/natija/{name}.jpg", template)


async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
