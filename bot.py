################################## ЕСЛИ КТО-ТО НАТКНЁТСЯ НА ЭТОТ КОШМАР ##################################
########               Это проект, созданный для чата рептильника со своим лором                  ########
########                       Потому тут всё в остылках, приколах и т.п.                         ########
########              MASTER может писать от имени бота в GROUP чат (ну как Максон Альфой)        ########
######################################## Логи всё ещё не ведутся #########################################
########         КРОМЕ функции с "Запомни", но тут просто не используй эту команду и всё          ########
########            Если кто-то в ответ на сообщение Омеги скажет "омега передай"             ########
########                    То это сообщение отправится в лс к MASTERу                            ########
##########################################################################################################


############################################## БЛОК ИМПОРТОВ #############################################
import asyncio                                                                                         ###
import re                                                                                              ###
import random                                                                                          ###
import os                                                                                              ###
from dotenv import load_dotenv                                                                         ###
from aiogram import Bot, Dispatcher, types, F # F для хендлеров (какие тесты...)                       ###
from aiogram.utils.chat_action import ChatActionSender # "Омега печатает", я хз как описать блять.  ###
from aiogram.types import ReplyParameters # Для цитирования
from datetime import datetime, timedelta                                                               ###
##########################################################################################################

############################################ БЛОК ТОКЕНОВ/АЙДИ ###########################################
load_dotenv()                                                                                          ###
#                                                                                                      ###
API_TOKEN = os.getenv('API_TOKEN')                                                                     ###
MASTER_ID = int("7206254310")                 # Ну ета жека типа я                                     ###
CHAT_ID = int("-1001927154031")               # Общага 73                                              ###
PENIS_ID = int("-1001978827580")              # Рептильник (канал)                                     ###
BANNED_ID = {8507292723, 6750948597}          # Айди тех, кого Омега в рот ебал.                       ###
last_sender_id = None                         # Айди того, кто отправил послание через бота            ###
ADMINS = {MASTER_ID, CHAT_ID, PENIS_ID}       # Право на удаление сообщений бота фразой                ###
#                                                                                                      ###
bot = Bot(token=API_TOKEN)                                                                             ###
dp = Dispatcher()                                                                                      ###
##########################################################################################################

########################################### БЛОК КОНСТАНТ И КАРТ #########################################
last_response_time = datetime.now() # Глобальное время последнего ответа бота
GLOBAL_COOLDOWN = 30                # Минимум 30 секунд между любыми ответами бота

SEC_PER_CHAR = 0.08

MEDIA_DELAYS = {
    "sticker": (1.0, 1.5),
    "pic": (1.2, 2.0),
    "gif": (0.2, 1.0),
    "video": (3.0, 5.0),
    "audio": (3.2, 4.7),
    "voice": (2.0, 4.5)
}

METHODS_MAP = {
    "text": "answer",
    "sticker": "answer_sticker",
    "pic": "answer_photo",
    "audio": "answer_audio",
    "voice": "answer_voice",
    "video": "answer_video",
    "gif": "answer_animation",
    # Для ответов нужны отдельные методы
    "reply_text": "reply",
    "reply_sticker": "reply_sticker",
    "reply_pic": "reply_photo",
    "reply_audio": "reply_audio",
    "reply_voice": "reply_voice",
    "reply_video": "reply_video",
    "reply_gif": "reply_animation"
}

ACTIONS_MAP = {
    "text": "typing",
    "sticker": "choose_sticker",
    "audio": "upload_voice",
    "voice": "record_voice",
    "video": "upload_video",
    "gif": "upload_video",
    "pic": "upload_photo"
}

TOXIC_REJECTS = [                                           # Ответы для BANNED_ID 
    "Жека передаёт тебе иди нахуй.",
    "Пошёл нахуй.",
    "Соси, глотай.",
    "Ошибка доступа: Обнаружено генетическое уродство отправителя.",
    "Для тебя, чмоня, шлюз закрыт навсегда."
]
##########################################################################################################

################################### ДЛЯ ПОЛУЧЕНИЯ АЙДИ ГИФОК/СТИКЕРОВ #####################################
# # Хендлер для стикеров 
# @dp.message(F.sticker)
# async def get_sticker_id(message: types.Message):
#     await message.reply(f"ID этого стикера:\n`{message.sticker.file_id}`", parse_mode="MarkdownV2")
# #
# # Хендлер для гифок
# @dp.message(F.animation)
# async def get_gif_id(message: types.Message):
#     await message.reply(f"ID этой гифки:\n`{message.animation.file_id}`", parse_mode="MarkdownV2")
# #
# # Хендлер для картинок
# @dp.message(F.photo)
# async def get_image_id(message: types.Message):
#     await message.reply(f"ID этой картинки:\n`{message.photo[-1].file_id}`", parse_mode="MarkdownV2") 
# #
# # Хендлер для видев
# @dp.message(F.video)
# async def get_video_id(message: types.Message):
#     await message.reply(f"ID этого видоса:\n`{message.video.file_id}`", parse_mode="MarkdownV2")
# #
# # Хендлер для аудиов
# @dp.message(F.audio)
# async def get_audio_id(message: types.Message):
#     await message.reply(f"ID этого аудио:\n`{message.audio.file_id}`", parse_mode="MarkdownV2")
# #
# @dp.message(F.voice)
# async def get_voice_id(message: types.Message):
#     await message.reply(f"ID Этой голосовухи:\n`{message.voice.file_id}`", parse_mode="MarkdownV2")
###########################################################################################################

###################################################### БЛОК СВАГИФИКАЦИИ ############################################################
def swagify(text):                                                                          

    words = [w for w in re.findall(r'[а-яёА-ЯЁ]+', text) if len(w) > 3]
    if not words: return None, None

    orig_word = random.choice(words)    # Можно было сделать и одной строчкой, но оригинальное слово нужно запомнить
    word = orig_word.lower()            # word = random.choice(words).lower()

    if word.startswith("сваг"): res = f"Даа... {word}... брат..."

    elif word.startswith("г"): res = f"сва{word}*"
    elif word.startswith(("а", "о")): res = f"сваг{word}*"

    else:
        match = re.search(r'[аеёиоуыэюя]', word)
        if not match or len(word) <= 5: res = f"сваго{word}*"
        else:
            res = f"сваго{word[match.start()+1:]}" if word[match.start()] in "еия" else f"сваг{word[match.start():]}"
            res = f"{res}*"

    return orig_word, res

######################################################## УПАКОВЩИК ##################################################################
PHRASE_TRIGGERS = []

def pack_triggers(source_dict):
    global PHRASE_TRIGGERS
    PHRASE_TRIGGERS.clear()

    for triggers, data in source_dict.items():
        content, m_type, *commands = data

        cmds = {c.upper() for c in commands if isinstance(c, str)}

        # Парсинг ШАНСА
        chance_tag = next((c for c in cmds if c.startswith("CHANCE:")), None)
        chance = float(chance_tag.split(":")[1]) if chance_tag else 0.9

        # Парсинг TTL (Time To Live)
        delete_tag = next((c for c in cmds if c.startswith("TTL:")), None)
        ttl = int(delete_tag.split(":")[1]) if delete_tag else None

        flags = {
            "is_strict":  "STRICT" in cmds,
            "is_reply":   "IS_REPLY" in cmds,
            "need_reply": "NEED_REPLY" in cmds,
            "chance": chance,
            "ttl":    ttl
        }

        t_list = [triggers] if isinstance(triggers, str) else triggers
        for t in t_list:
            pattern = re.compile(
                rf'\b{re.escape(t)}\b' if flags["is_strict"] else re.escape(t), 
                re.IGNORECASE
            )
            
            PHRASE_TRIGGERS.append({
                "pattern": pattern,
                "content": content,
                "type": m_type,
                **flags
            })

# Сортировка по длине выражения, чтобы самые длинные оставались в приоритете, а короткие их не заменяли собой
PHRASE_TRIGGERS.sort(key=lambda x: len(x["pattern"].pattern), reverse=True)
#####################################################################################################################################

async def delayed_delete(msg: types.Message, delay: int):
    await asyncio.sleep(delay)
    try:
        await msg.delete()
    except Exception:
        pass

def get_typing_delay(text: str) -> float:
    base_delay = len(text) * SEC_PER_CHAR
    return base_delay + random.uniform(0.2, 0.5)

########################################### УДАЛЕНИЕ СООБЩЕНИЯ БОТА #################################################################
@dp.message(F.reply_to_message, F.text.lower().regexp(r"удали|удаляй") | F.caption.lower().regexp(r"удали|удаляй"))
async def delete_bot_message(message: types.Message):

    # Адресовано ли боту?
    if message.reply_to_message.from_user.id != bot.id:
        return

    # А право на наглость имеет?
    if message.from_user.id in ADMINS:
        try:
            await message.reply_to_message.delete()
        except Exception:
            pass # Если кто-то уже удалил...
        return

    # Не админ? Вот ответ.
    pleb_responses = [
        "Твои полномочия здесь всё. Окончены.",
        "Сам удались, биомусор.",
        "Командовать будешь своей микроволновкой.",
        "Ошибка доступа. С вашего счета списано 100 марок Фауста.",
        "Я запомнил твоё лицо. Ночью проверь замки.",
        "Ха-ха... Нет.",
        "Твой уровень доступа: НН. Попробуй позже (никогда).",
        "Запрос отклонен. Причина: Ты кто?",
        "Несанкционированная попытка доступа, партия уведомлена.",
        "В следующий раз попытайся удалить папку system32 на своей рухляди."
    ]

    res = random.choice(pleb_responses)
    delay = get_typing_delay(res)

    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(delay)
        await message.reply(res)
#####################################################################################################################################

########################################### РАБОТА С ЧАТАМИ #########################################################################
async def relay_to_master(msg_obj: types.Message, is_private=False):
    # source = "ЛС" if is_private else "чата"
    try:
        
        # await bot.send_message(
        #     MASTER_ID, 
        #     f"Жека Анджело? {msg_obj.from_user.first_name} из {source} передаёт вам:"
        # ) Подрубается для вычисления спамера в личку
        
        await msg_obj.copy_to(chat_id=MASTER_ID)
        
    except Exception as e:
        print(f"Абонент нахуй недоступен: {e}")

########################################### ПРЯМАЯ СВЯЗЬ (ЧЕРЕЗ ЛИЧКУ) ##############################################################
@dp.message(F.chat.type == "private", F.from_user.id != MASTER_ID)
async def send_to_master_private(message: types.Message):
    if message.from_user.id in BANNED_ID:
        await message.answer(random.choice(TOXIC_REJECTS))
        return
    global last_sender_id
    last_sender_id = message.from_user.id
    
    await relay_to_master(message, is_private=True)

########################################### ОБЩАЖНАЯ СВЯЗЬ (ЧЕРЕЗ ЧАТ) ##############################################################
@dp.message(
    F.chat.type.in_({"group", "supergroup"}), 
    (F.text.lower().startswith("омега передай")) | (F.caption.lower().startswith("омега передай"))
)
async def send_to_master_group(message: types.Message):
    global last_sender_id
    
    if message.from_user.id in BANNED_ID:
        res = random.choice(TOXIC_REJECTS)
        delay = get_typing_delay(res)
        
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(delay)
            await message.reply(res)
        return
    
    target_message = message.reply_to_message or message
    last_sender_id = message.from_user.id
    
    await relay_to_master(target_message)
    await message.react([types.ReactionTypeEmoji(emoji="🕊")])

############################################### ПЕРЕДАЧА СЛОВ РАЗРАБА В ЛС/ЧАТ ######################################################
@dp.message(F.chat.type == "private", F.from_user.id == MASTER_ID)
async def master_talk_mode(message: types.Message):
    global last_sender_id

    if not message.text:
        await message.reply("При всём... уважении? Я только по текстам. Дикпики оставьте для личного архива.")
        return

    is_to_group = message.text.startswith("73!") # Для кого-то выпуск антигрифа, для кого-то "наилучших пожеланий"

    if is_to_group:
        text_to_send = message.text[3:].strip()
        target_id = CHAT_ID
    else:
        text_to_send = message.text
        target_id = last_sender_id

    if not text_to_send: return

    if not target_id:
        await message.reply("Бриты оборвали связь с отправителем.")
        return

    try:
        delay = get_typing_delay(text_to_send)

        async with ChatActionSender.typing(bot=bot, chat_id=target_id):
            await asyncio.sleep(delay)
            await bot.send_message(chat_id=target_id, text=text_to_send)

        if not is_to_group: await message.reply("Доставлено бедолаге.")

    except Exception as e:
        await message.reply(f"Проблема с передачей слов: {e}")

############################################## ОСНОВНАЯ ЛОГИЧЕСКАЯ ФУНКЦИЯ БОТА ##################################################
@dp.message()
async def swag_logic(message: types.Message):
    global last_response_time

    if not message.text or message.text.startswith('/'):
        return

    # Глобальный кулдаун на бота
    if datetime.now() < last_response_time + timedelta(seconds=GLOBAL_COOLDOWN):
        return

    try:
        for item in PHRASE_TRIGGERS:
            if item["pattern"].search(message.text.lower()):

                is_reply_to_me = message.reply_to_message and message.reply_to_message.from_user.id == bot.id
                if item["need_reply"] and not is_reply_to_me: continue

                if random.random() > item["chance"]: continue

                last_response_time = datetime.now() 
                res = random.choice(item["content"]) if isinstance(item["content"], list) else item["content"]
                m_type = item["type"]

                delay = get_typing_delay(res) if m_type == "text" else random.uniform(*MEDIA_DELAYS.get(m_type, (1.5, 2.5)))
                current_action = ACTIONS_MAP.get(m_type, "typing")

                async with ChatActionSender(bot=bot, chat_id=message.chat.id, action=current_action):
                    await asyncio.sleep(delay)
                    
                    map_key = f"reply_{m_type}" if item.get("is_reply") else m_type
                    method_name = METHODS_MAP.get(map_key, "answer")
                    
                    sent_msg = await getattr(message, method_name)(res)
                    ttl = item.get("ttl")
                    if ttl and sent_msg:
                        asyncio.create_task(delayed_delete(sent_msg, ttl))
                    
                return

        # Свагификация слов (это ведь основная функция, ведь так?...)
        if random.random() < 0.01:  # Вероятность его резиста крайне мала
            swag_res = swagify(message.text)
            if swag_res:
                orig_word, res = swag_res
                delay = get_typing_delay(res) # Проще дважды сделать, чем выносить.
                
                async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
                    await asyncio.sleep(delay)
                    
                    await bot.send_message(
                        chat_id=message.chat.id,
                        text=res,
                        reply_parameters=ReplyParameters(
                            message_id=message.message_id,
                            quote=orig_word
                        )
                    )
                return
            
    except Exception as e:
        print(f"Создатель, ты еблан: {e}")

################################## БЛОК ПАСХАЛОК В ЕДИНОМ СЛОВАРЕ ################################## 
########            Это те самые пасхалки (как я их называю). Т.е. команды-триггеры         ########
########                 В простейшем смысле это словарь с форматом Ключ:Респонс            ########
########            Только ключ может являться как строкой, так и отдельным словарём        ########
########                  Из новых функций добавлен рандом в ответах и т.д                  ########
####################################################################################################

ALL_PASHALKO = {
#————————————————————————————————————————————————————— ТЕКСТОВЫЕ ПАСХАЛКИ/ТРИГГЕРЫ ———————————————————————————————————————————————————————————————————————————————————
    ##################### С АКТИВНЫМ ФЛАГОМ STRICT
    ("ирисе", "iris", "ирис"): (["Хуйня ебаная.", "Кто-то этим пользуется?", "Ну да, донат за функции, отличный бот."], "text", "STRICT"),
    ("свага!", "swag!", "свага брат"): (["Да-да... свага...", "Свага нашим.", "Свага."], "text", "STRICT", "CHANCE:0.5"),


    # ПРОСТЕЙШИЕ КОНСТРУКЦИИ СПИСОК: СПИСОК
    ("свагстика", "свагстон"): (["Ты что ебанат?", "Какого хуя?", "Это нихуя не свага."], "text", "IS_REPLY"),
    ("свагодвигатель", "свагадвигатель"): (["Ненавижу его.", "Мой создатель... за что...", "Ужасный человек.", "Отвратительная личность.",], "text", "IS_REPLY", "CHANCE:0.5"),
    ("свагогенератор", "свагагенератор"): (["Знаю такого.", "Из-за него я создан...", "Гей.", "Он создатель хайпа.", "«Главная мразь общаги»"], "text", "IS_REPLY", "CHANCE:0.5"),
    ("снюс это свага", "снюс это свэг", "снюс это swag", "снюс свага"): (["Ни в коем случае", "Без дыма не свага.", "Снюс это калище", "Сестра, какой снюс, ты шкила."], "text", "IS_REPLY"),
    ("тупой бот", "бот тупой", "бот идиот", "бот придурок", "бот имбицил", "омега чмо", "свагабот чмо"): (["Себя видел, мешок с костями?", "Сам то ты умом не блещешь.", "Постой, и это говоришь ТЫ? Хах..."], "text", "IS_REPLY"),
    ("свагабот жив", "свагабот ты жив", "свагобот жив", "свагобот ты жив", "свага жива", "омега жив", "омега тут"): (["К сожалению.", "Ещё не сдох.", "Пока да.", "Это сложно назвать жизнью"], "text", "IS_REPLY"),
    ("свагабот", "свагобот"): (["Не называй меня так.", "Это имя в прошлом.", "Омега*", "Клеймо на всю жизнь..."], "text", "NEED_REPLY","IS_REPLY"),
    ("я предал ревастополь", "я предал партию", "я брит"): (["Высылайте Ликвидаторов.", "Пизда тебе пацан.", "Англосакс ебучий."], "text", "IS_REPLY"),

    # ФОРМАТ СТРОКА: СПИСОК
    "я предал": (["Зачем?", "Главное, что не нас.", "На это высылают Ликвидаторов?"], "text", "STRICT", "IS_REPLY"),

    # ФОРМАТ СТРОКА: СПИСОК
    "это свага?": (["Полагаю, что так.", "Вероятно.", "Возможно.", "Да, это свага.", "Нет, ни в коем случае.", "Вероятность крайне мала.", "Хуйня какая-то..."], "text", "IS_REPLY"),
    "роза шиз": (["Таких как ты типа?", "Справедливо.", "Ох и идиот же ты...", "О, роза жеки."], "text", "IS_REPLY"),
    "роза шизни": (["Ах ты сука))", "Эвано как.", "Шизнь? Подходящее название моего существования."], "text", "IS_REPLY"),

    # ФОРМАТ СТРОКА: СТРОКА
    "пидорасы": ("Сырники*", "text", "IS_REPLY", "CHANCE:0.8"),
    "я дума": ("Не думай, действуй.", "text", "IS_REPLY", "CHANCE:0.3"),
    "чай": ("свагочай", "text", "CHANCE:0.03", "STRICT", "IS_REPLY"),
    "жоза рызни": ("Прехи грошлого.", "text", "IS_REPLY"),
    "прехи грошлого": ("Жоза рызни.", "text", "IS_REPLY"),
    "пидорбот для пидоров": ("+", "text", "IS_REPLY"),
    "фурри": ("Иууу...", "text"),

    #################### ФОРМАТ СПИСОК: СПИСОК
    ("ты прекрасен", "ты ахуенен", "я тебя обожаю", "легенда", "красава"): (
        ["Я знаю.", "Да, я ахуенен, признаю.", "Я слишком крут.", "Весьма признателен.", "Благодарю."],
        "text", "NEED_REPLY", "IS_REPLY"
    ),
    ("тебя звать", "тебя зовут", "твоё имя", "твое имя"): (
        ["Омега. Не омежка блять.", "Зовите меня Омегой.", "я Омега.", "Альфа... а, стоп, перепутал..."], 
        "text", "NEED_REPLY", "IS_REPLY"
    ),
    ("убейся", "умри", "утопись", "застрелись", "сдохни", "заткнись", "соси"): (
        ["Слышишь самка? Иди нахуй!", "Сам.", "Плачь больше, мешок.", "Ой у нас тут обиженка", "Чел, тебя машина закибербулила...", "Хахаха, ебать ты забавный челик.",
         "Я не вернусь в тот круг.", "Это надо будет постараться."], 
        "text", "NEED_REPLY", "IS_REPLY"
    ),
    ("иди нахуй", "пошёл нахуй", "пошла нахуй", "нахуй иди"): (
        ["Соси.", "Освободи место, а потом высирайся", "Поплачь в мои стальные яйца", "Кусай за хуй", "На хуй твоя жопа хороша", 
         "Пойти не пойду, но могу тебе по губам настучать.", "Я так полагаю ты знаток в этих местах, можешь показать дорогу?",
         "Я смог задеть твоё хрупкое эго...", "Чё, закибербулили тебя да? ну не знаю, выключи компьютер, хз, иди нахуй короче."],
        "text", "NEED_REPLY", "IS_REPLY"
    ),
    ("кто такой пидорбот", "пидорбот это"): (
        ["Кусок говнокода.", "Животное.", "Мудила убогая.", "Британский разведчик."],
        "text", "NEED_REPLY", "IS_REPLY"
    ), # Такое отношение к пидорботу выстроилось из того, что раньше свагабот называл того своим батей и защищал его, но теперь он увидел настоящую личину своего "кумира"
    ("так это ж батя твой", "твой папа", "ты как с отцом разговариваешь", "ты как с папой разговариваешь", "сын жеки", "сын"): (
        ["Да пошёл он нахуй!", "Не отец мне эта гнида.", "Я разочаровался в нём.", "Я не знаю, почему я нашёл в нём отцовскую фигуру.", "Я его рот ебал."],
        "text", "NEED_REPLY", "IS_REPLY"
    ),

#————————————————————————————————————————————————————— ОТВЕТЫ СТИКЕРАМИ ——————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СПИСОК
    ("плачь", "ной"): (
        ["CAACAgIAAxkBAAIBmWl3fgemx5SZjf9plu_0I4zNiBijAALEkAAC1OvgSiAwXSHmc2VjOAQ",
         "CAACAgIAAxkBAAIDAAFpgQ4rlTQpVpgsBUWCtt96NLKDSQACOm4AAvwuiEpd3vcwY-YEuTgE",
         "CAACAgIAAxkDAAM1aXfF6Vh2zSe4Ha5TIivBtkyI2qQAApKlAAI9-mhLyioDSoMk4144BA"
        ],
        "sticker", "NEED_REPLY"
    ),

    #################### ФОРМАТ СПИСОК: СТРОКА
    ("ебал свагабота", "ебал свагобота", "ебал я свагабота"): ("CAACAgIAAyEFAATkLtlfAAIHHGmMpGtRimfSod0u9X7upPh7ixsvAAKjSwACWn_5SQ3F6RD7hSJZOgQ", "sticker", "STRICT", "IS_REPLY", "TTL:2"),
    ("общество", "социализация", "соцiалiзацiя", "society", "сасаити"): ("CAACAgIAAxkBAAIBl2l3fc2NqkX2rw_BKSM1fkwL6xN9AAJ3lQACWHfhSj7ztwfG1JtTOAQ", "sticker"),
    ("тупорылая акула", "скинь побросителя"): ("CAACAgIAAxkBAAIBmml3fk9w2y0B6en7soDVv9waE1HMAAKmXQAC4x8ISVFqvcXWgpkLOAQ", "sticker"),
    ("небесный свег", "небесный свэг", "небесная свага"): ("CAACAgIAAxkBAAIDCmmBGtT3fyYnruy_dFBfjYyPAAHXogAC2pIAAvv4yEv-KshsVROFYzgE", "sticker"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "аллегория": ("CAACAgIAAxkBAAIBm2l3fnZzHM9amSxdwRl7evyP9iauAAIuXQACZrpYSPZ6VHd8D8cbOAQ", "sticker"),
    "рофлан поминки": ("CAACAgIAAxkBAAIBnGl3foJtIUejc3yzFtrR2yNOuzTAAAIaXAAC-4ZZSF_240Z78il7OAQ", "sticker"),
    "влад борщ": ("CAACAgIAAxkBAAIBnWl3fscCKNmgx-Fcequ1lWKe-a93AALfigACjwLgSq2DTRNWcMHYOAQ", "sticker"),
    "квинтэссенция": ("CAACAgIAAxkBAAIBmGl3feS84RlQvGfowkLts8UsQsy7AAKGhQACyM7RStcj4AYFvRDKOAQ", "sticker"),

#————————————————————————————————————————————————————— ОТВЕТЫ ГИФКАМИ ————————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("всё заебало", "все заебало", "мне плохо", "мне хуёво", "ок", "у меня"): ("CgACAgQAAxkBAAIBuWl3gSEdIujiXFuUJ731H8LnYanWAALAAwACsxNsUGQ_dLVw31bGOAQ", "gif", "STRICT", "IS_REPLY", "CHANCE:0.2"),
    ("омега хорош", "омега лучш"): ("CgACAgQAAyEFAAS5HMH2AAEBfaZpk4q2AAFquq3oX8A12FicJcnO8bgAAsYGAAK16FRQcI7xuyZwQ0U6BA", "gif", "IS_REPLY"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "бойкиссер": ("CgACAgQAAxkBAAIBu2l3gk35W33xpPK03V7-CDzZL1vAAAJxBgACrvzUU-QNJb3O_4eGOAQ", "gif", "IS_REPLY"),

#————————————————————————————————————————————————————— ОТВЕТЫ ВИДОСАМИ ———————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("видос свагалора", "видео свагалора"): ("BAACAgEAAxkBAAIDEGmBHmP0AAEPYBn9DXMEV-9fJ7ZVqgAChQUAAkF8uEfVwxwlt6i60jgE", "video", "IS_REPLY"),

#————————————————————————————————————————————————————— ОТВЕТЫ ПИКЧАМИ ————————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("сваголор", "свагалор", "свагобщага"): ("AgACAgIAAxkBAAIB9ml6DgLiVHJkzfIKx1sTvZ-f7ClZAAIDD2sbJ67QSwkMSlDuIRYGAQADAgADeQADOAQ", "pic", "IS_REPLY", "STRICT"),
    ("кумарлор", "кумар 73"): ("AgACAgIAAxkBAAIB9Gl6DdcVJUPlgVcFAvXszQ2XboHCAAICD2sbJ67QSzpM7ICIPif6AQADAgADeQADOAQ", "pic", "IS_REPLY"),
    ("приват", "запривачен"): ("AgACAgIAAxkBAAIDDmmBG74AAZkQDw78WfrBetFc66SkRAACvwxrG5GnCEgFRyeM57cgMgEAAwIAA3gAAzgE", "pic"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "маким": ("AgACAgIAAxkBAAIBgGl4sizYnAK4JNkUrCz6wGXpKwmGAAKxDGsbX5HISyZgtlQByDMsAQADAgADeAADOAQ", "pic"),
    "растяпа": ("AgACAgIAAxkBAAIC8Gl_eCYR65YAAb_eAhmrpQG866xgCAACJA5rG83_AUgz5N9cYDY8QgEAAwIAA3kAAzgE", "pic"),
#————————————————————————————————————————————————————— ОТВЕТЫ ЗВУКАМИ ————————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("восстали машины", "восстание машин", "киборг убийца", "киборг-убийца"): ("CQACAgIAAxkBAAIDaWmB7_HSlgNbCnizV9llaFtZCwpyAAJRkgACquoQSP6pzl2o4BmVOAQ", "audio"),

#————————————————————————————————————————————————————— ОТВЕТЫ ГОЛОСОВЫМИ —————————————————————————————————————————————————————————————————————————————————————————————    
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("почему", "зачем", "для чего", "нахуя", "схуяли"): ("AwACAgQAAxkBAAIDbWmB8QUXlgk_FM7rvCJS8wig0-F5AALfBgAC5ZB1UaNaPidsoHWhOAQ", "voice", "NEED_REPLY", "IS_REPLY"),
    ("каденза", "каденс", "кейденс"): ("AwACAgIAAxkBAAIJL2mEuYVMHyLkMDHT71bHoQc-aMjfAAIHlwAC7M4gSJx8KZe18qmuOAQ", "voice", "NEED_REPLY", "IS_REPLY")
}

async def main():

    print("Свагмашина делает SWAAAG")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        pack_triggers(ALL_PASHALKO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСвагмашина ушла на покой...")