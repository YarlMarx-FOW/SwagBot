import asyncio
import re
import random
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F # F для тестов
from datetime import datetime, timedelta

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Пропишу здесь, это защита от спама.
user_cooldowns = {}
COOLDOWN_SECONDS = 30

def swagify(text):

    words = re.findall(r'[а-яёА-ЯЁ]+', text)
    if not words:
        return None

    word = random.choice(words).lower()
    vowels = "аеёиоуыэюя"
    # Логика процесса свагинации состоит из if if if if
    # А ты че хотел?))

    # точные совпадения и исключения лелеле
    exceptions = {
        "свингер": "Я отказываюсь это комментировать",
        "вагина": "свагина... блять..." # мне стыдно
    }
    if word in exceptions:
        return exceptions[word]

    if word.startswith("сваг"):
        return f"Лютейши {word}, брат"
    
    # префиксы
    if word.startswith("г"):
        return f"сва{word}"

    if word.startswith("о"):
        return f"сваг{word}"
    
    # по длине
    if len(word) <= 2:
        return None
    if len(word) == 3:
        return f"сваго{word}"
    
    # Поиск первой гласной
    match = re.search(f"[{vowels}]", word)
    if match:
        i = match.start()
        char = word[i]
        
        if char in "еи":
            return f"сваго{word[i+1:]}"
        return f"сваг{word[i:]}"       
    return f"сваго{word}"

STRICT_BANS = {"сво", "зов"} # Strict потому что в слове свобода есть сво, а бот как псих эти 3 буквы везде видел
BAN_WORDS = ["гитлер", "1488", "грехи прошлого", "роза жизни", "порно", "свастика"] # Думаю очевидно что это

#################################### БЛОК ПАШАЛОК/КОМАНД Я ХЗ КАК ЭТО ОПИСАТЬ ##############################
STRICT_PASHALKI = {
    "роза": "Вы любите розы? А я на них срал!",
    "свага!": "СВАГААА БРААТ!!!",
    "свагогенератор": "Брат мой ваще крутой!",
    "свагодвигатель": "Создатель за что??!??",
    "свагстика": "Не одобряем! Сваголоврат тоже, вроде...",
    "убейся": "Сам."
}
PASHALKI = {
    "роза шизни": "Ах ты сука)",
    "роза шиз": "Таких как ты типа?",
    "свагабот ты прекрасен": "Ты тоже братанчик!",
    "свагабот ты ахуенен": "и пиздат, зацените мой прикид.",
    "свагабот жив?": "Свага не умрёт!",
    "свагабот ты жив?": "Свага не умрёт!",
    "кто такой пидорбот": "Это папа мой.",
    "пидорбот для пидоров": "Не оскорбляй моего батю!",
    "свагабот": "Свага на месте.",
    "свагобот": "Свагабот*",
    "тупой бот": "Себя видел? Мешок с костями.",
    "это свага?": "Лютейшая, брат!",
    "фурри": "Иууу...",
    "для пидоров": "+",
    "я предал": "Как ты мог..."
} 
GIF_PASHALKИ = {
    "всё заебало": "CgACAgQAAxkBAAIBuWl3gSEdIujiXFuUJ731H8LnYanWAALAAwACsxNsUGQ_dLVw31bGOAQ",
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
    "свагобот для пидоров": "CAACAgIAAxkBAAIBi2l3enTd-Mavr1mFpolgULxK1ztiAALtjwAC0O_RSvqpL0UwcxW3OAQ",
    "свагабот для пидоров": "CAACAgIAAxkBAAIBi2l3enTd-Mavr1mFpolgULxK1ztiAALtjwAC0O_RSvqpL0UwcxW3OAQ"
}


#################################### ТАК КАК ПАШАЛОК МНОГО, ЛУЧШЕ ТУТ ОДИН РАЗ ПРОГНАТЬ ####################
PHRASE_TRIGGERS = []

for t, c in PASHALKI.items(): PHRASE_TRIGGERS.append((t, c, "text"))
for t, c in STICKER_PASHALKИ.items(): PHRASE_TRIGGERS.append((t, c, "sticker"))
for t, c in GIF_PASHALKИ.items(): PHRASE_TRIGGERS.append((t, c, "gif"))

PHRASE_TRIGGERS.sort(key=lambda x: len(x[0]), reverse=True)
#################################### ДЛЯ ПОЛУЧЕНИЯ АЙДИ ГИФОК/СТИКЕРОВ #####################################
# Хендлер для стикеров 
# @dp.message(F.sticker)
# async def get_sticker_id(message: types.Message):
#     await message.reply(f"ID этого стикера:\n`{message.sticker.file_id}`", parse_mode="MarkdownV2")
#
# Хендлер для гифок
# @dp.message(F.animation)
# async def get_gif_id(message: types.Message):
#     await message.reply(f"ID этой гифки:\n`{message.animation.file_id}`", parse_mode="MarkdownV2")
############################################################################################################

@dp.message()
async def swag_logic(message: types.Message):
    try:

        ######################## Блок защиты от спама ###################################
        user_id = message.from_user.id
        now = datetime.now()
        if user_id in user_cooldowns:
            if now < user_cooldowns[user_id] + timedelta(seconds=COOLDOWN_SECONDS):
                return 
        user_cooldowns[user_id] = now

        # Если пусто или команда — шкип
        if not message.text or message.text.startswith('/'):
            return

        msg_low = message.text.lower()

        ######################## ДЛЯ ЗАПРЕТОК ААААААААА #################################
        its_all_bad = [(w, True) for w in STRICT_BANS] + [(w, False) for w in BAN_WORDS]
        for bad_word, is_strict in its_all_bad:
            pattern = rf'\b{re.escape(bad_word)}\b' if is_strict else re.escape(bad_word)
            match = re.search(pattern, msg_low)
            if match:
                original = message.text[match.start():match.end()]
                await message.answer(
                    text="ты че еблан что ли?",
                    reply_parameters=types.ReplyParameters(message_id=message.message_id, quote=original)
                )
                return
        ######################## Блок шикарных пасхалок #################################
        user_words = set(re.findall(r'[а-яё0-9?!]+', msg_low))

        # Извиняйся. Т.е. ответы на ответ ну да.
        if message.reply_to_message:
            reply_text = message.reply_to_message.text or ""
            # Проверка ответов через простой словарь (чтобы как дурак не плодить if/elif)
            responses = {
                "ПОТИШЕ, БРАТАНЧИК": (["сорри", "прости", "извини"], "Та ниче, бывает, свага."),
                "ты че еблан что ли?": (["да"], "sticker:CAACAgIAAxkBAAIBgml3eNYTs9Plv3rYfJVNHjzWd52BAAKSpQACPfpoS8oqA0qDJONeOAQ"),
                "Не одобряем!": (["пиздабол", "пиздит", "врет", "лжет"], "Ой да иди ты нахуй!")
            }
            
            for key, (triggers, answer) in responses.items():
                if key in reply_text and any(t in msg_low for t in triggers):
                    if answer.startswith("sticker:"):
                        await message.reply_sticker(answer.split(":")[1])
                    else:
                        await message.reply(answer)
                    return
                
        for trigger, s_id in STICKER_PASHALKИ.items():
            if trigger in msg_low:
                await message.reply_sticker(sticker=s_id)
                return
            
        # Это делается для того, чтобы бот условно не вырывал слово "роза" из слова "розариум" + хотел попробовать set()
        found_strict = user_words.intersection(STRICT_PASHALKI.keys()) 
        if found_strict:
            trigger = list(found_strict)[0]
            await message.reply(STRICT_PASHALKI[trigger])
            return
            
        for trigger, content, media_type in PHRASE_TRIGGERS:
        # Для гифок — строгий поиск границы слова, для остального — вхождение
            if media_type == "gif":
                match = re.search(rf'\b{re.escape(trigger)}\b', msg_low)
            else:
                match = trigger in msg_low

            if match:
                if media_type == "sticker":
                    await message.reply_sticker(sticker=content)
                elif media_type == "gif":
                    await message.reply_animation(animation=content)
                else:
                    await message.reply(content)
                return
            
        if message.text.isupper() and len(message.text) > 25:
            await message.reply("ПОТИШЕ, БРАТАНЧИК")
            return

        ######################## Рандомная свагинация ###################################
        if random.random() < 0.01:
            result = swagify(message.text)

            if result:
                await message.reply(result)

    except Exception as e:
        print(f"Ошибка в сваго-двигателе: {e}")

async def main():

    print("Свагмашина делает SWAAAG")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСвагмашина ушла на покой...")

# теперь код выглядит так, как ты хотел, хочешь, накидаем простую систему АХАХХА НАЕБАЛ АХАХАХХАХА