import os
from dotenv import load_dotenv

############################################ БЛОК ТОКЕНОВ/АЙДИ ###########################################
load_dotenv()                                                                                          ###
# Токен и айдишники                                                                                    ###
API_TOKEN = os.getenv('API_TOKEN')                                                                     ###
MASTER_ID = int(os.getenv('MASTER_ID', 0))       # Ну ета жека типа я                                  ###
CHAT_ID = int(os.getenv('CHAT_ID', 0))           # Общага 73                                           ###
PENIS_ID = int(os.getenv('PENIS_ID', 0))         # Рептильник (канал)                                  ###
PHANTOM_ID = int(os.getenv('PHANTOM_ID', 0))     # ССССударь                                           ###
# Посылание нахуй                                                                                      ###
BANNED_IDS = set(map(int, [i for i in os.getenv('BANNED_IDS', '').split(',') if i.strip().isdigit()])) ###
ADMINS = {MASTER_ID, CHAT_ID, PENIS_ID, PHANTOM_ID} # Право на удаление сообщений бота фразой          ###
# Константы для чата                                                                                   ###
GLOBAL_COOLDOWN = 30                # Минимум 30 секунд между любыми ответами бота                     ###
SEC_PER_CHAR = 0.08                 # Время на символ                                                  ###
##########################################################################################################