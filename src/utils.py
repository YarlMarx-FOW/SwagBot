##########################################################################################################
########               Это проект, созданный для чата рептильника со своим лором                  ########
########                       Потому тут всё в остылках, приколах и т.п.                         ########
########              MASTER может писать от имени бота в GROUP чат (ну как Максон Альфой)        ########
######################################## Логи всё ещё не ведутся #########################################
########         КРОМЕ функции с "Запомни", но тут просто не используй эту команду и всё          ########
########            Если кто-то в ответ на сообщение Омеги скажет "омега передай"                 ########
########                    То это сообщение отправится в лс к MASTERу                            ########
##########################################################################################################


import re
import random
import asyncio
import state
from aiogram import types
from init_bot import bot
from config import SEC_PER_CHAR, MASTER_ID
import state

######################################################## УПАКОВЩИК ##################################################################

def pack_triggers(source_dict):
    state.PHRASE_TRIGGERS.clear()

    for triggers, data in source_dict.items():
        content, m_type, *commands = data

        cmds = {c.upper() for c in commands if isinstance(c, str)}

        # Парсинг ШАНСА
        chance_tag = next((c for c in cmds if c.startswith("CHANCE:")), None)
        chance = float(chance_tag.split(":")[1]) if chance_tag else 0.6

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
            
            state.PHRASE_TRIGGERS.append({
                "pattern": pattern,
                "content": content,
                "type": m_type,
                **flags
            })

# Сортировка по длине выражения, чтобы самые длинные оставались в приоритете, а короткие их не заменяли собой
state.PHRASE_TRIGGERS.sort(key=lambda x: len(x["pattern"].pattern), reverse=True)
#####################################################################################################################################

############################################# ЗАДЕРЖКА РАЗВИТИЯ (ТИПА ПЕЧАТАНИЯ) ####################################################
def get_typing_delay(text: str) -> float:
    base_delay = len(text) * SEC_PER_CHAR
    return base_delay + random.uniform(0.2, 0.5)

###################################################### ЧИСКА СЛЕДОВ (TTL) ###########################################################
async def delayed_delete(msg: types.Message, delay: int):
    await asyncio.sleep(delay)
    try:
        await msg.delete()
    except Exception:
        pass

######################################################## РАБОТА С ЧАТАМИ ############################################################
async def relay_to_master(msg_obj: types.Message, is_private=False):

    try:
        
        await bot.send_message(
            MASTER_ID, 
            f"Жека Анджело? {msg_obj.from_user.first_name} {msg_obj.from_user.last_name} [{state.last_sender_id}] передаёт вам:"
         ) # Подрубается для вычисления спамера в личку
        
        await msg_obj.copy_to(chat_id=MASTER_ID)
        
    except Exception as e:
        print(f"Абонент нахуй недоступен: {e}")

######################################################## БЛОК СВАГИФИКАЦИИ ##########################################################
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