import asyncio
import re
import random
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F # F для тестов

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def swagify(text):

    words = re.findall(r'[а-яёА-ЯЁ]+', text)
    if not words:
        return None

    word = random.choice(words).lower()
    vowels = "аеёиоуыэюя"
    # Логика процесса свагинации состоит из if if if if
    # А ты че хотел?))
    if word.startswith("сваг"):
        return f"Да, это {word}"
    
    if word.startswith("г"):
        return f"сва{word}"

    if word.startswith("о"):
        return f"сваг{word}"
    
    if word.startswith("свингер"):
        return f"Я отказываюсь это комментировать."

    if len(word) <= 4:
        return f"сваго{word}"

    for i, char in enumerate(word):

        if char in vowels:

            if char in "еи":
                return f"сваго{word[i+1:]}"
            
            return f"сваг{word[i:]}"
        
    return f"сваго{word}"

BAN_WORDS = ["гитлер", "1488", "сво", "грехи прошлого", "роза жизни", "порно", "свастика"] # Думаю очевидно что это
#################################### На них бот реактит всегда ###########################
PASHALKI = {
    "свагобот": "Свага на месте.",
    "пидорбот": "Это папа мой.",
    "СВАГА": "СВАГААА БРААТ!!!",
    "это свага?": "Лютейшая, брат!",
    "ты прекрасен": "Ты тоже братанчик!",
    "ты ахуенен": "и пиздат, зацените мой прикид.",
    "жив?": "Свага не умрёт!",
    "ты жив?": "Свага не умрёт!",
    "свагстика": "Не одобряем! Сваголоврат тоже, вроде...",
    "убейся": "Сам.",
    "фурри": "Иууу...",
    "роза шизни": "Ах ты сука)",
    "роза": "Вы любите розы? А я на них срал!"
} 
GIF_PASHALKИ = {
    "ок": "CgACAgQAAxkBAAIBuWl3gSEdIujiXFuUJ731H8LnYanWAALAAwACsxNsUGQ_dLVw31bGOAQ",
    "бойкиссер": "CgACAgQAAxkBAAIBu2l3gk35W33xpPK03V7-CDzZL1vAAAJxBgACrvzUU-QNJb3O_4eGOAQ"
}
STICKER_PASHALKИ = {
    "поплачь": "CAACAgIAAxkBAAIBmWl3fgemx5SZjf9plu_0I4zNiBijAALEkAAC1OvgSiAwXSHmc2VjOAQ",
    "тупорылая акула": "CAACAgIAAxkBAAIBmml3fk9w2y0B6en7soDVv9waE1HMAAKmXQAC4x8ISVFqvcXWgpkLOAQ",
    "аллегория": "CAACAgIAAxkBAAIBm2l3fnZzHM9amSxdwRl7evyP9iauAAIuXQACZrpYSPZ6VHd8D8cbOAQ",
    "рофлан поминки": "CAACAgIAAxkBAAIBnGl3foJtIUejc3yzFtrR2yNOuzTAAAIaXAAC-4ZZSF_240Z78il7OAQ",
    "влад борщ": "CAACAgIAAxkBAAIBnWl3fscCKNmgx-Fcequ1lWKe-a93AALfigACjwLgSq2DTRNWcMHYOAQ",
    "квинтэссенция": "CAACAgIAAxkBAAIBmGl3feS84RlQvGfowkLts8UsQsy7AAKGhQACyM7RStcj4AYFvRDKOAQ",
    "общество": "CAACAgIAAxkBAAIBl2l3fc2NqkX2rw_BKSM1fkwL6xN9AAJ3lQACWHfhSj7ztwfG1JtTOAQ",
    "свагобот для пидоров": "CAACAgIAAxkBAAIBi2l3enTd-Mavr1mFpolgULxK1ztiAALtjwAC0O_RSvqpL0UwcxW3OAQ"
}

#################################### ДЛЯ ПОЛУЧЕНИЯ АЙДИ ГИФОК/СТИКЕРОВ #####################################
# Хендлер для стикеров 
# @dp.message(F.sticker)
# async def get_sticker_id(message: types.Message):
#     await message.reply(f"ID этого стикера:\n`{message.sticker.file_id}`", parse_mode="MarkdownV2")
#
# # Хендлер для гифок
# @dp.message(F.animation)
# async def get_gif_id(message: types.Message):
#     await message.reply(f"ID этой гифки:\n`{message.animation.file_id}`", parse_mode="MarkdownV2")
############################################################################################################
@dp.message()
async def swag_logic(message: types.Message):

    # Если пусто или команда — шкип
    if not message.text or message.text.startswith('/'):
        return

    msg_low = message.text.lower()

    ######################## ДЛЯ ЗАПРЕТОК ААААААААА #################################
    for bad_word in BAN_WORDS:

        if bad_word in msg_low:
            start_index = msg_low.find(bad_word)
            original_word = message.text[start_index : start_index + len(bad_word)]

            await message.answer(
                text="ты че еблан что ли?",
                reply_parameters=types.ReplyParameters(
                    message_id=message.message_id,
                    quote=original_word
                )
            )
            return

    ######################## Блок шикарных пасхалок #################################
    for trigger, s_id in STICKER_PASHALKИ.items():
        if trigger in msg_low:
            await message.reply_sticker(sticker=s_id)
            return
    for trigger, response in PASHALKI.items():
        if trigger in msg_low:
            await message.reply(response)
            return
    for trigger, g_id in GIF_PASHALKИ.items():
        if trigger in msg_low:
            await message.reply_animation(animation=g_id)
            return   
        
    if message.text.isupper() and len(message.text) > 5:
        await message.reply("ПОТИШЕ, БРАТАНЧИК")
        return

    # Извиняйся.
    if message.reply_to_message:
        if "ПОТИШЕ, БРАТАНЧИК" in message.reply_to_message.text:
            if any(word in msg_low for word in ["сорри", "прости", "извини"]):
                await message.reply("Та ниче, бывает, свага.")
                return
            
        if "ты че еблан что ли?" in message.reply_to_message.text:
            if msg_low == "да":
                sticker_id = "CAACAgIAAxkBAAIBgml3eNYTs9Plv3rYfJVNHjzWd52BAAKSpQACPfpoS8oqA0qDJONeOAQ" 
                await message.reply_sticker(sticker=sticker_id)
                return
            
    ######################## Рандомная свагинация ###################################
    if random.random() < 0.05:
        result = swagify(message.text)

        if result:
            await message.reply(result)

async def main():

    print("Свагошина делает SWAAAG")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())