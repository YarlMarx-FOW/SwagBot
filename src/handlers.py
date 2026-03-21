from aiogram import Router, F, types
import random
import asyncio
import state

from aiogram.types import ReplyParameters
from aiogram.utils.chat_action import ChatActionSender
import utils    
import config
import constants
from init_bot import bot
from datetime import datetime, timedelta

router = Router()

########################################### УДАЛЕНИЕ СООБЩЕНИЯ БОТА #################################################################
@router.message(F.reply_to_message, F.text.lower().regexp(r"удали|удаляй") | F.caption.lower().regexp(r"удали|удаляй"))
async def delete_bot_message(message: types.Message):

    # Адресовано ли боту?
    if message.reply_to_message.from_user.id != bot.id:
        return

    # А право на наглость имеет?
    if message.from_user.id in config.ADMINS:
        try:
            await message.reply_to_message.delete()
        except Exception:
            pass # Если кто-то уже удалил...
        return

    # Не админ? Вот ответ.
    
    res = random.choice(constants.PLEB_RESPONSES)
    delay = utils.get_typing_delay(res)

    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(delay)
        await message.reply(res)
#####################################################################################################################################

########################################### ПРЯМАЯ СВЯЗЬ (ЧЕРЕЗ ЛИЧКУ) ##############################################################
@router.message(F.chat.type == "private", F.from_user.id != config.MASTER_ID)
async def send_to_master_private(message: types.Message):
    if message.from_user.id in config.BANNED_IDS:
        await message.answer(random.choice(constants.TOXIC_REJECTS))
        return
    global last_sender_id
    state.last_sender_id = message.from_user.id
    
    await utils.relay_to_master(message, is_private=True)
#####################################################################################################################################

########################################### ОБЩАЖНАЯ СВЯЗЬ (ЧЕРЕЗ ЧАТ) ##############################################################
@router.message(
    F.chat.type.in_({"group", "supergroup"}), 
    (F.text.lower().startswith("омега передай")) | (F.caption.lower().startswith("омега передай"))
)
async def send_to_master_group(message: types.Message):
    global last_sender_id
    
    if message.from_user.id in config.BANNED_IDS:
        res = random.choice(constants.TOXIC_REJECTS)
        delay = utils.get_typing_delay(res)

        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            await asyncio.sleep(delay)
            await message.reply(res)
        return
    
    target_message = message.reply_to_message or message
    state.last_sender_id = message.from_user.id
    
    await utils.relay_to_master(target_message)
    await message.react([types.ReactionTypeEmoji(emoji="🕊")])
#####################################################################################################################################

############################################### ПЕРЕДАЧА СЛОВ РАЗРАБА В ЛС/ЧАТ ######################################################
@router.message(F.chat.type == "private", F.from_user.id == config.MASTER_ID)
async def master_talk_mode(message: types.Message):
    global last_sender_id

    if not message.text:
        await message.reply("При всём... уважении? Я только по текстам. Дикпики оставьте для личного архива.")
        return

    is_to_group = message.text.startswith("73!") # Для кого-то выпуск антигрифа, для кого-то "наилучших пожеланий"

    if is_to_group:
        text_to_send = message.text[3:].strip()
        target_id = config.CHAT_ID
    else:
        text_to_send = message.text
        target_id = state.last_sender_id

    if not text_to_send: return

    if not target_id:
        await message.reply("Бриты оборвали связь с отправителем.")
        return

    try:
        delay = utils.get_typing_delay(text_to_send)

        async with ChatActionSender.typing(bot=bot, chat_id=target_id):
            await asyncio.sleep(delay)
            await bot.send_message(chat_id=target_id, text=text_to_send)

        if not is_to_group: await message.reply("Доставлено бедолаге.")

    except Exception as e:
        await message.reply(f"Проблема с передачей слов: {e}")
#####################################################################################################################################

############################################## ОСНОВНАЯ ЛОГИЧЕСКАЯ ФУНКЦИЯ БОТА #####################################################
@router.message()
async def swag_logic(message: types.Message):

    if not message.text or message.text.startswith('/'):
        return

    # Глобальный кулдаун на бота
    if datetime.now() < state.last_response_time + timedelta(seconds=config.GLOBAL_COOLDOWN):
        return

    try:
        for item in state.PHRASE_TRIGGERS:
            if item["pattern"].search(message.text.lower()):

                is_reply_to_me = message.reply_to_message and message.reply_to_message.from_user.id == bot.id
                if item["need_reply"] and not is_reply_to_me: continue

                if random.random() > item["chance"]: continue

                state.last_response_time = datetime.now() 
                res = random.choice(item["content"]) if isinstance(item["content"], list) else item["content"]
                m_type = item["type"]

                delay = utils.get_typing_delay(res) if m_type == "text" else random.uniform(*constants.MEDIA_DELAYS.get(m_type, (1.5, 2.5)))
                current_action = constants.ACTIONS_MAP.get(m_type, "typing")

                async with ChatActionSender(bot=bot, chat_id=message.chat.id, action=current_action):
                    await asyncio.sleep(delay)
                    
                    map_key = f"reply_{m_type}" if item.get("is_reply") else m_type
                    method_name = constants.METHODS_MAP.get(map_key, "answer")
                    
                    sent_msg = await getattr(message, method_name)(res)
                    ttl = item.get("ttl")
                    if ttl and sent_msg:
                        asyncio.create_task(utils.delayed_delete(sent_msg, ttl))
                    
                return

        # Свагификация слов (это ведь основная функция, ведь так?...)
        if random.random() < 0.01:  # Вероятность его резиста крайне мала
            swag_res = utils.swagify(message.text)
            if swag_res:
                orig_word, res = swag_res
                delay = utils.get_typing_delay(res) # Проще дважды сделать, чем выносить.
                
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
#####################################################################################################################################