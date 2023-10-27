import asyncio
import cv2
from aiogram import F
from aiogram.types import *
from aiogram import Bot, Dispatcher
from markup import *
from aiogram.types import Message
import logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token="5997549250:AAHIwR6lVFzdoIqs7v5zUubOvS4mHzV8-RU")
arr = []


async def start(message: Message):
    img = FSInputFile("Certificate-shablon/certificate.png")
    await message.answer(
        f"Assalomu alekum {message.from_user.full_name} Sertifikat tayyorlaydigan botga xush kelibsiz!"
        f"Bu bot orqali o’zingizga sertifikat tayyorlab olishingiz mumkin.")
    await message.answer_photo(img, caption="Marhamat quyidagi sertifikatni o’zingizga moslab o’zgartiring/n"
                                            "Pastdagi inlinelar orqali ketma-ket amallarni bajarishingiz mukin",
                               reply_markup=bosh_kb)


async def one_level(message: Message):
    img = FSInputFile("Certificate-shablon/certificate-1.png")
    await message.answer_photo(img, caption="Boshladik")
    await message.answer("1-bosqich Bo'sh o'ringga yozuv yozing!")


async def two_level(message: Message):
    arr.append('two')
    img = FSInputFile("Certificate-shablon/certificate-2.png")
    await message.answer_photo(img)
    await message.answer("2-bosqich Bo'sh o'ringga yozuv yozing!")


async def three_level(message: Message):
    arr.append('three')
    img = FSInputFile("Certificate-shablon/certificate-3.png")
    await message.answer_photo(img)
    await message.answer("3-bosqich Bo'sh o'ringga yozuv yozing!")


async def four_level(message: Message):
    arr.append('four')
    img = FSInputFile("Certificate-shablon/certificate-4.png")
    await message.answer_photo(img)
    await message.answer("4-bosqich Bo'sh o'ringga yozuv yozing!")


async def five_level(message: Message):
    arr.append('five')
    img = FSInputFile("Certificate-shablon/certificate-5.png")
    await message.answer_photo(img)
    await message.answer("5-bosqich Bo'sh o'ringga yozuv yozing!")


async def six_level(message: Message):
    arr.append('six')
    img = FSInputFile("Certificate-shablon/certificate-6.png")
    await message.answer_photo(img)
    await message.answer("6-bosqich Bo'sh o'ringga yozuv yozing!")


async def seven_level(message: Message):
    arr.append('seven')
    img = FSInputFile("Certificate-shablon/certificate-7.png")
    await message.answer_photo(img)
    await message.answer("7-bosqich Bo'sh o'ringga yozuv yozing!")


async def eight_level(message: Message):
    arr.append('eight')
    img = FSInputFile("Certificate-shablon/certificate-8.png")
    await message.answer_photo(img)
    await message.answer("8-bosqich Bo'sh o'ringga yozuv yozing!")


async def nine_level(message: Message):
    arr.append('nine')
    img = FSInputFile("Certificate-shablon/certificate-9.png")
    await message.answer_photo(img)
    await message.answer("9-bosqich Bo'sh o'ringga yozuv yozing!")


async def one_message(message: Message):
    summa = 0
    print("one message", arr)
    for a in arr:
        if a == 'two':
            summa += 1

        if a == 'three':
            summa += 1

        if a == 'four':
            summa += 1

        if a == 'five':
            summa += 1

        if a == 'six':
            summa += 1

        if a == 'seven':
            summa += 1

        if a == 'eight':
            summa += 1

        if a == 'nine':
            summa += 1

    if summa == 0:
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
            await message.answer("1-bosqich tugadi davom ettiring!", reply_markup=one_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 1:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("2-bosqich tugadi davom ettiring!", reply_markup=two_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 2:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 104), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 104), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 104), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("3-bosqich tugadi davom ettiring!", reply_markup=three_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 3:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("4-bosqich tugadi davom ettiring!", reply_markup=four_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 4:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("5-bosqich tugadi davom ettiring!", reply_markup=five_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 5:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("6-bosqich tugadi davom ettiring!", reply_markup=six_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 6:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("7-bosqich tugadi davom ettiring!", reply_markup=seven_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 7:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("8-bosqich tugadi davom ettiring!", reply_markup=eight_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")

    if summa == 8:
        template = cv2.imread(f'Certificate-client/{message.from_user.id}.jpg')
        if 15 > len(message.text) >= 3:
            if 6 >= len(message.text) >= 3:
                cv2.putText(template, message.text, (230, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 12 > len(message.text) > 6:
                cv2.putText(template, message.text, (215, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            elif 15 >= len(message.text) >= 12:
                cv2.putText(template, message.text, (200, 68), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Muhammad/Desktop/Projects/Certificate/Certificate-client/{message.from_user.id}.jpg",
                        template)
            img = FSInputFile(f"Certificate-client/{message.from_user.id}.jpg")
            await message.answer_photo(img)
            await message.answer("9-bosqich tugadi davom ettiring!", reply_markup=nine_kb)
        elif len(message.text) < 3:
            await message.answer("Iltimos 3 ta harfdan kam ishlatilmasin")
        elif len(message.text) > 15:
            await message.answer("Iltimos 15 ta harfdan ko'p ishlatilmasin")


dp = Dispatcher()
dp.message.register(start, F.text == '/start')
dp.message.register(one_level, F.text == "Boshlash💥")
dp.message.register(two_level, F.text == "2-bosqichga o'tish")
dp.message.register(three_level, F.text == "3-bosqichga o'tish")
dp.message.register(four_level, F.text == "4-bosqichga o'tish")
dp.message.register(five_level, F.text == "5-bosqichga o'tish")
dp.message.register(six_level, F.text == "6-bosqichga o'tish")
dp.message.register(seven_level, F.text == "7-bosqichga o'tish")
dp.message.register(eight_level, F.text == "8-bosqichga o'tish")
dp.message.register(nine_level, F.text == "9-bosqichga o'tish")


dp.message.register(one_message, F.text != "2-boshqichga o'tish" or F.text != "3-boshqichga o'tish" or F.text != "3-boshqichga o'tish")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
