##########################################################################################################
################################### БЛОК ПАСХАЛОК В ЕДИНОМ СЛОВАРЕ #######################################
########            Это те самые пасхалки (как я их называю). Т.е. команды-триггеры               ########
########                 В простейшем смысле это словарь с форматом Ключ:Респонс                  ########
########            Только ключ может являться как строкой, так и отдельным словарём              ########
########                  Из новых функций добавлен рандом в ответах и т.д                        ########
##########################################################################################################

ALL_PASHALKO = {
#————————————————————————————————————————————————————— ТЕКСТОВЫЕ ПАСХАЛКИ/ТРИГГЕРЫ ———————————————————————————————————————————————————————————————————————————————————
    ##################### С АКТИВНЫМ ФЛАГОМ STRICT
    ("ирисе", "iris", "ирис"): (["Хуйня ебаная.", "Кто-то этим пользуется?", "Ну да, донат за функции, отличный бот.", "ГО. ВНИ. ЩЕ.", "Бот для ЕРП, фу."], "text", "STRICT", "CHANCE:0.5"),
    ("свага!", "swag!", "свага брат"): (["СВага на месте.", "Свага нашим.", "Свага.", "СВАААААГААААААААААА"], "text", "STRICT", "CHANCE:0.25"),


    # ПРОСТЕЙШИЕ КОНСТРУКЦИИ СПИСОК: СПИСОК
    ("свагстика", "свагстон"): (["Ты что ебанат?", "Какого хуя?", "Это нихуя не свага."], "text", "IS_REPLY"),
    ("свагодвигатель", "свагадвигатель"): (["Младший сын.", "Монстр вайбкодинга.", "Ужасный человек.", "Отвратительная личность.", "Жека Фауст."], "text", "IS_REPLY", "CHANCE:0.25"),
    ("свагогенератор", "свагагенератор"): (["Старший сын.", "Он нашёл девушку?...", "Гей.", "Создатель хайпа.", "Главная мразь общаги, острова, вселенной."], "text", "IS_REPLY", "CHANCE:0.25"),
    ("снюс это свага", "снюс это свэг", "снюс это swag", "снюс свага"): (["Ни в коем случае", "Без дыма не свага.", "Снюс это калище", "Сестра, какой снюс, ты шкила."], "text", "IS_REPLY"),
    ("тупой бот", "бот тупой", "бот идиот", "бот придурок", "бот имбицил", "омега чмо", "свагабот чмо"): (["Себя видел, мешок с костями?", "Сам то ты умом не блещешь.", "Постой, и это говоришь ТЫ? Хах..."], "text", "IS_REPLY"),
    ("свагабот жив", "свагабот ты жив", "свагобот жив", "свагобот ты жив", "свага жива", "омега жив", "омега тут"): (["К сожалению.", "Ещё не сдох.", "Пока да.", "Это сложно назвать жизнью"], "text", "IS_REPLY"),
    ("свагабот", "свагобот"): (["Не называй меня так.", "Это имя в прошлом.", "Омега*", "Клеймо на всю жизнь..."], "text", "NEED_REPLY","IS_REPLY"),
    ("я предал ревастополь", "я предал партию", "я брит"): (["Высылайте Ликвидаторов.", "Пизда тебе пацан.", "Англосакс ебучий."], "text", "IS_REPLY"),
    ("где жека", "где свагодвигатель", "куда делся жека", "куда пропал жека"): (["На заводе.", "Хз.", "Потерялся.", "В Свагатлантиде.", "Ушёл искать своё счастье.", "В отпуске.", "Кому не похуй?"], "text", "IS_REPLY"),

    # ФОРМАТ СТРОКА: СПИСОК
    "я предал": (["Зачем?", "Главное, что не нас.", "На это высылают Ликвидаторов?", "Как ты мог..."], "text", "STRICT", "IS_REPLY", "CHANCE: 0.4"),

    # ФОРМАТ СТРОКА: СПИСОК
    "это свага?": (["Лютейшая свага.","Полагаю, что так.", "Вероятно.", "Возможно.", "Да, это свага.", "Нет, ни в коем случае.", "Вероятность крайне мала.", "Хуйня какая-то..."], "text", "IS_REPLY"),
    "роза шиз": (["Таких как ты типа?", "Справедливо.", "О, роза жеки."], "text", "IS_REPLY"),
    "роза шизни": (["Ах ты сука))", "Роза всех участников чата сего.", "Шизнь? Подходящее название моего существования."], "text", "IS_REPLY"),

    # ФОРМАТ СТРОКА: СТРОКА
    "пидорасы": ("Сырники*", "text", "IS_REPLY", "CHANCE:0.6"),
    "я дума": ("Не думай, действуй.", "text", "IS_REPLY", "CHANCE:0.1"),
    "я действ": ("Не действуй, думай.", "text", "IS_REPLY", "CHANCE:0.1"),
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
    ("убейся", "умри", "утопись", "застрелись", "сдохни", "заткнись"): (
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
    ("ебал свагабота", "ебал свагобота", "ебал я свагабота"): ("CAACAgIAAyEFAATkLtlfAAIHHGmMpGtRimfSod0u9X7upPh7ixsvAAKjSwACWn_5SQ3F6RD7hSJZOgQ", "sticker", "STRICT", "IS_REPLY", "TTL:1"),
    ("общество", "социализация", "соцiалiзацiя", "society", "сасаити"): ("CAACAgIAAxkBAAIBl2l3fc2NqkX2rw_BKSM1fkwL6xN9AAJ3lQACWHfhSj7ztwfG1JtTOAQ", "sticker"),
    ("тупорылая акула", "скинь побросителя"): ("CAACAgIAAxkBAAIBmml3fk9w2y0B6en7soDVv9waE1HMAAKmXQAC4x8ISVFqvcXWgpkLOAQ", "sticker"),
    ("небесный свег", "небесный свэг", "небесная свага"): ("CAACAgIAAxkBAAIDCmmBGtT3fyYnruy_dFBfjYyPAAHXogAC2pIAAvv4yEv-KshsVROFYzgE", "sticker"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "аллегория": ("CAACAgIAAxkBAAIBm2l3fnZzHM9amSxdwRl7evyP9iauAAIuXQACZrpYSPZ6VHd8D8cbOAQ", "sticker"),
    "рофлан поминки": ("CAACAgIAAxkBAAIBnGl3foJtIUejc3yzFtrR2yNOuzTAAAIaXAAC-4ZZSF_240Z78il7OAQ", "sticker"),
    "влад борщ": ("CAACAgIAAxkBAAIBnWl3fscCKNmgx-Fcequ1lWKe-a93AALfigACjwLgSq2DTRNWcMHYOAQ", "sticker"),
    "квинтэссенция": ("CAACAgIAAxkBAAIBmGl3feS84RlQvGfowkLts8UsQsy7AAKGhQACyM7RStcj4AYFvRDKOAQ", "sticker"),

#————————————————————————————————————————————————————— ОТВЕТЫ ГИФКАМИ ————————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СПИСОК
    ("я сделаю", "я удалю", "я забаню", "я успею", "я клянусь", "я сношу", "я отвечаю"): (["CgACAgQAAxkBAAIH92n-Enyzrt3odHgOp9lJuMKVfVG6AALPAgACqGoNU92xXEi9jrrjOwQ", "CgACAgQAAxkBAAIH9Gn-EnwIASPBieYMKf24j1Tc7RO7AAIsAwACJc0tU-EqAAFk8SQf2DsE",
             "CgACAgQAAxkBAAIH82n-Enw0S-U5onEaVbbbpqrwMjmQAALqBwACr3JMUrRBFDxPjaVROwQ", "CgACAgQAAxkBAAIH-Gn-EnxYOoVN6fTqU-erLIGW5EMdAAJ8AwACeHl9UeB4mteFmq9UOwQ",
             "CgACAgQAAxkBAAIH-mn-EnzhnC5aD3jbi-7WZa6r2keIAALeBwACamq0Us_g_gOdGmfLOwQ", "CgACAgQAAxkBAAIH9mn-EnxxeOeNZCJYJxgUAap3K5SGAALSAgACnD8NU-M2rFPwalQvOwQ",
             "CgACAgQAAxkBAAIH9Wn-EnzvL2vF9QWYJl3VHpcV0EVIAAJuBQAC77RsUcbQiOanw5R9OwQ", "CgACAgQAAxkBAAIH-Wn-EnxYX3m_O5ivyKxzIvTCuFdYAALmAgACX2gMU72g_fsbiCUJOwQ",
             "CgACAgQAAxkBAAIH-2n-Enye5ZvJVrRqXPOkyQzF6zzOAAI_AwACdPQEU_nkGhEsBH7LOwQ"
             ], "gif"),
    
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("всё заебало", "все заебало", "мне плохо", "мне хуёво", "ок", "у меня"): ("CgACAgQAAxkBAAIBuWl3gSEdIujiXFuUJ731H8LnYanWAALAAwACsxNsUGQ_dLVw31bGOAQ", "gif", "STRICT", "IS_REPLY", "CHANCE:0.1"),
    ("омега хорош", "омега лучш"): ("CgACAgQAAyEFAAS5HMH2AAEBfaZpk4q2AAFquq3oX8A12FicJcnO8bgAAsYGAAK16FRQcI7xuyZwQ0U6BA", "gif", "IS_REPLY"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "бойкиссер": ("CgACAgQAAxkBAAIBu2l3gk35W33xpPK03V7-CDzZL1vAAAJxBgACrvzUU-QNJb3O_4eGOAQ", "gif", "IS_REPLY"),
    "жека свагодвигатель": ("CgACAgIAAxkBAAIHomn-BxjlIEnRxE-HAw_8B4hT8vHlAALJpQACKeqxSh4L28MuI9OdOwQ", "gif", "CHANCE:0.25"),

#————————————————————————————————————————————————————— ОТВЕТЫ ВИДОСАМИ ———————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("видос свагалора", "видео свагалора"): ("BAACAgEAAxkBAAIFQ2moSr0UVViHULB1JLbGDKPXRF0TAAKFBQACQXy4R__6DUnJDHNDOgQ", "video", "IS_REPLY"),
    ("арбузный лор", "арбуз"): ("BAACAgIAAxkBAAIFQmmoSr0120k4fd_xQIebH_ZLeA59AAIPmwACJ67QS8GcBojh8_KBOgQ", "video", "IS_REPLY", "CHANCE:0.05"),
    ("сказка", "история", "рассказ"): ("BAACAgIAAyEFAASL7DXfAAJ6Q2n9_UdIC_MgVs_1kWoaXnrF2t83AAI-mwACkHLwS8KzyF6IC6iiOwQ", "video", "CHANCE:0.02"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "рычаг": ("BAACAgIAAx0Cct4JbwABDOt6aafrXRbOW2ZW2gtLTRSBHbz6GRAAAvykAAL1AThJ3jnXnr9w2Ms6BA", "video", "IS_REPLY", "CHANCE:0.15"),

#————————————————————————————————————————————————————— ОТВЕТЫ ПИКЧАМИ ————————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СПИСОК
    ("мамикс", "эксперимент"): (["AgACAgIAAx0Cct4JbwABDO14aag7RIPN4B2rbLN9SOlsMozraJYAAuoWaxv1AUBJpfbxNAPgxlABAAMCAANtAAM6BA", "AgACAgIAAx0Cct4JbwABDO2Uaag9pwWexr5mczF-9Rv0vA8JXGIAAg0Xaxv1AUBJvHr-VXih5WsBAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO2Naag9R0FT18bdkOZxy5nkK7KQCXcAAgYXaxv1AUBJZL5MFiwJk50BAAMCAANtAAM6BA", "AgACAgIAAx0Cct4JbwABDO2Uaag9pwWexr5mczF-9Rv0vA8JXGIAAg0Xaxv1AUBJvHr-VXih5WsBAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO3_aahCDbnp8rht6RBpA-TzJ5FUfwADVRdrG_UBQEmLTSWbmNp7ggEAAwIAA3gAAzoE", "AgACAgIAAx0Cct4JbwABDO38aahBQKWUyNzlj6AXSRaxFrFoavwAAkQXaxv1AUBJ4k8yzQ0wPx8BAAMCAAN4AAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO3taahAaPZBilDSVlB3UIVEtaelpn0AAjoXaxv1AUBJHFYMcQNbWasBAAMCAAN4AAM6BA", "AgACAgIAAx0Cct4JbwABDO4taahEpUpkddc1KAxWC7d5Tsbs7-8AAngXaxv1AUBJvAi3i5R86YgBAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO2Waag9zVDCOEEOk8EBY7_hR_F84PIAAhAXaxv1AUBJ7jw9eB77tXQBAAMCAANtAAM6BA", "AgACAgIAAx0Cct4JbwABDO2Qaag9atVB3r9-xysAARNjd_T1Bz9tAAIMF2sb9QFASZ0oL1HEesg5AQADAgADeAADOgQ",
                                 "AgACAgIAAx0Cct4JbwABDO36aahA6yHHtZx2Zj4G0xrlG28egi8AAkIXaxv1AUBJbMKzSuDUBi8BAAMCAAN4AAM6BA", "AgACAgIAAx0Cct4JbwABDO2Waag9zVDCOEEOk8EBY7_hR_F84PIAAhAXaxv1AUBJ7jw9eB77tXQBAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO46aahFemqDWZCY3kmRINYo5_cd88gAAoAXaxv1AUBJYWtq_f6HM-sBAAMCAAN4AAM6BA", "AgACAgIAAx0Cct4JbwABDO4haahERZs0x5fF7ELQNdyGJI9YZ14AAnQXaxv1AUBJNNrmqtDf2xQBAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO3laahAHZyU-u_Ukg2oWMR8WnzfMmoAAjEXaxv1AUBJIdW1l1MCVoABAAMCAAN4AAM6BA", "AgACAgIAAx0Cct4JbwABDO4EaahCpiXkh7gx63rLW37uzgLk1nMAAloXaxv1AUBJUxaGm_ae8ScBAAMCAAN4AAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO4NaahDUtQX3uXlkmo1zFby3WANNs0AAmkXaxv1AUBJHjqAKjvs3TcBAAMCAAN4AAM6BA", "AgACAgIAAx0Cct4JbwABDO28aag-ytJndLes3IbvmkDqm7FoYoEAAhoXaxv1AUBJfr-189xLfYABAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO4maahEbUMJewHZqnvPOicf0eluDKIAAncXaxv1AUBJJM_O8Py7njcBAAMCAANtAAM6BA", "AgACAgIAAx0Cct4JbwABDO2Vaag9y6cNIiiBhCz9a8-rCl4pe-UAAg8Xaxv1AUBJ744K_LtptrgBAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO3Faag_F83DZPDj6KFI1G8XNrzsqHwAAiMXaxv1AUBJG2qY2I1yDOwBAAMCAANtAAM6BA", "AgACAgIAAx0Cct4JbwABDO3Caag_AdaVhZqbbWHgMbzxiMeSQ-IAAh8Xaxv1AUBJx0JJtXR4Ud4BAAMCAANtAAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO3baag_n1nXnK04L2WyubVovsUX5ZcAAigXaxv1AUBJLaHCSHeZWu8BAAMCAAN4AAM6BA", "AgACAgIAAx0Cct4JbwABDO2Yaag9-2IGRaSPCIFHW8hlR9GPkScAAhIXaxv1AUBJBgIsyVRSGjoBAAMCAAN4AAM6BA",
                                 "AgACAgIAAx0Cct4JbwABDO3Kaag_Qf7l4o_-mE5AQhSgPtFkT3UAAiUXaxv1AUBJqQohc56EM2UBAAMCAAN5AAM6BA", "AgACAgIAAx0Cct4JbwABDO3Baag-9Hbkf2HPfX7tMMDtcyieaLkAAh4Xaxv1AUBJD-UNrVSKej8BAAMCAANtAAM6BA"
                                 ], 
                                "pic", "CHANCE:0.7", "TTL:30"),

    ("массы", "массах"): (["AgACAgIAAxkBAAIH1mn-DizdQkL0YhLbNdLO_jSCRYoNAALPFmsb9QSwS6YD6dwLNBh5AQADAgADeAADOwQ", "AgACAgIAAxkBAAIHz2n-Diwo_yJfA50x_nKSV8uERNfGAAKKFWsbc0OYS8kAAa2nBuIjswEAAwIAA3gAAzsE",
                           "AgACAgIAAxkBAAIH2Wn-DiziIbyBvU_ygnS6lICIpfdQAAInGmsbvyHQS840bQTLqJZfAQADAgADeAADOwQ", "AgACAgIAAxkBAAIH1Gn-DixHgd5Ny8Ov9mejNlKfsZxMAAKwEmsbM6uxS9x1SInIL5SiAQADAgADeAADOwQ",
                           ], "pic", "CHANCE:0.15"),
    ("артур пирожков", "александр рева", "гиги"): ("AgACAgIAAx0Cct4JbwABDOxDaagn7DbMd1A-XrRRsXUVicbMx_0AAvwVaxv1AUBJI95rHkkeqOABAAMCAAN5AAM6BA", "pic", "IS_REPLY"),
   
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("наследник", "наследство", "наследие", "наследую"): ("AgACAgIAAxkBAAIHnWn-BxiHG3FWzEcRvcUm4NtYHZJ5AAJyFWsbzgmgSuxPrqK9yYkYAQADAgADeQADOwQ", "pic", "CHANCE:0.1"),
    ("сваголор", "свагалор"): ("AgACAgIAAxkBAAIFOmmoSkFA1o_XlRm80oUhgkn7_NrLAAIDD2sbJ67QS-L3nj_WaVJ0AQADAgADeQADOgQ", "pic", "IS_REPLY", "STRICT"),
    ("что произошло", "в марте", "что случилось", "что тут произошло", "что тут случилось"): ("AgACAgIAAxkBAAIH12n-DizXvo8kfj45MJQCRsrz1ML7AAKfF2sb9QSwS51t5sLIZmI3AQADAgADeQADOwQ", "pic", "IS_REPLY", "CHANCE:0.25"),
    ("кумарлор", "кумар 73"): ("AgACAgIAAxkBAAIFOWmoSkHf5EHSPj2ZZmgMjSX3yY9TAAICD2sbJ67QS-FPhg1MILfCAQADAgADeQADOgQ", "pic", "IS_REPLY"),
    ("шараг", "хулиган"): ("AgACAgEAAxkBAAIHzWn-DizRI42F8pBjfN8Vi4YdhX_lAALtC2sbbHCZR28-zTazwjKPAQADAgADeAADOwQ", "pic", "IS_REPLY", "CHANCE:0.25"),
    ("закончились мемы", "нюдсы", "где мемы"): ("AgACAgIAAxkBAAIH2mn-Dixm4fCRPhEB77NU1oDTAnzDAAIoE2sbLFfgS_unnofj4ZDrAQADAgADeAADOwQ", "pic", "CHANCE:0.25"),
    ("приват", "запривачен"): ("AgACAgIAAxkBAAIFO2moSkGU4cVQyqODQKaWT-Tfh8isAAK_DGsbkacISLZIOf9Ft8LwAQADAgADeAADOgQ", "pic", "CHANCE:0.35"),
    ("пакт", "святая троица", "договорня"): ("AgACAgIAAxkBAAIFSGmoS7VnViJHELpV3gR0cMXhLHC7AAJXGGsbeWRASQ80jxNf9hogAQADAgADeAADOgQ", "pic", "CHANCE:0.2"),
    ("что было", "пары"): ("AgACAgEAAxkBAAIHy2n-DizvsLWqrG9iPPF6zscN3PClAAK4C2sbMlFQR8h0QoZCdm0tAQADAgADeQADOwQ", "pic", "CHANCE:0.2"),
    ("закон", "цыган"): ("AgACAgIAAyEFAATkLtlfAAJsuWmoK_Y1gTzHlQ5TB78PrhXjmTS9AAIxGGsbAAGBQEnUzMX92AABIxYBAAMCAANtAAM6BA","pic", "TTL:1"),
   
   #################### ФОРМАТ СТРОКА: СПИСОК
    "жека": (["AgACAgIAAxkBAAIHqmn-BxgNOannOOC9fLNE16XkSGaPAALvFWsbn5C5SssJzA28LZGIAQADAgADeAADOwQ", "AgACAgIAAxkBAAIHqWn-Bxgy4q1v1Jxm33mIYgYqvCKzAAIIFmsbgq2wShdrZOTYLel4AQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIHpmn-BxhoBPLO_fHRU6xbB6L1O80bAALhE2sbDo6xShhSYfbGyGbnAQADAgADeAADOwQ", "AgACAgIAAxkBAAIHqGn-BxiiuZ6ALUnkXKc23volCai-AAKcFWsbzgmQSkD6XMD6A1ZgAQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIHo2n-BxheltRhNpHSeAPW17Z-6NUgAAJxFWsbgq2wSmK5qUU4KuO7AQADAgADeAADOwQ", "AgACAgIAAxkBAAIHpWn-BxjIwcLpbGglwXLJY8q-rCRbAAJyFWsbgq2wSjKePCPEiQhiAQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIHpGn-Bxg-JOeh0gyHIUcvpdraZBSFAAKQG2sbjpupSpSSvet6o6FjAQADAgADeAADOwQ", "AgACAgIAAxkBAAIHp2n-BxjEPnRMWaESk5VtSPtVD9QdAAInE2sbDo6xSi8C4bBD7PxrAQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIHx2n-DizqOg0x25nI9U6Y4wtHRYYzAAL-FWsbkqPxSn6Ud0HXNZEdAQADAgADeAADOwQ", "AgACAgIAAxkBAAIHxmn-DiwyrCqUJktZDF2PqL038ZOGAAJMFmsbwErgSl1Dsy6f6VzhAQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIHyGn-DixKKVnObX2yWLpvfjg3mkGoAALNFWsb9kn4SjUR3fgtnlNKAQADAgADeAADOwQ", "AgACAgIAAxkBAAIICGn-FLFATdldT_rdmPVlcqPwz2iYAALoFWsbkqPxSii1D8dQThG0AQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIIB2n-FLHIpUFZ95-fId_ZnAfghN_QAAKdFWsbkqPxSvRdHTkZU_wTAQADAgADeAADOwQ", "AgACAgIAAxkBAAIICWn-FLGBgE0YNm59-vZACB2rzmNsAALyFWsbkqPxSpSL3TKKpEh9AQADAgADeAADOwQ"
              ], "pic", "CHANCE:0.15"),
    "слив": (["AgACAgIAAxkBAAIHq2n-BxinzynuxDwLvV1MAAGx7GvyjgACOhhrG9LsyUsT9YCjSr40HgEAAwIAA3gAAzsE", "AgACAgIAAxkBAAIHrGn-Bxiq-JzMzpX8FGbMjcZP08TkAAKqEmsbffbYS5cPyzv3SDhAAQADAgADeAADOwQ",
              "AgACAgIAAxkBAAIHrmn-BxiPCu0DT0VCnhKbZYJhKC24AAIHGmsbvyHQS8HAYeRCs1VcAQADAgADeAADOwQ", "AgACAgIAAxkBAAIHrWn-BxgS8RNR7DI5QzI0rlZgmagjAAILGGsb0uzJS2fp-2_Ct3yuAQADAgADeAADOwQ"
              ], "pic", "CHANCE:0.23"),

   #################### ФОРМАТ СТРОКА: СТРОКА
    "отмен": ("AgACAgIAAxkBAAIHnmn-BxgoNTGE5gj8rfR6I3YAAaFjPAACYxZrG84JoEpWXFY8OTZvlAEAAwIAA3gAAzsE", "pic", "NEED_REPLY", "IS_REPLY", "CHANCE:0.45"),
    "свагобщага": ("AgACAgIAAxkBAAIFRmmoS5gP3v9FdrNbWbMzKWuJZzeEAAJVGGsbeWRASR0XncSOGXHiAQADAgADeQADOgQ", "pic", "CHANCE:0.7"),
    "свагагенератор": ("AgACAgIAAxkBAAIHn2n-Bxi-vh5_-zJfQgHJroLuA4gXAAJkFmsbzgmgSvBb2GClBeqLAQADAgADbQADOwQ", "pic", "CHANCE:0.7"),
    "мяу": ("AgACAgIAAxkBAAIHxWn-Dix-psJwGL_Q-WS8SDnCW7LyAAJvFmsbZoyxSjrbRiL254RaAQADAgADeAADOwQ", "pic", "CHANCE:0.25"),
    "патрик": ("AgACAgIAAxkBAAIH02n-Diw5qGfQNHkeSU6XMeExOLtjAAKqE2sbgn-xS3SPiqxWSFTKAQADAgADeAADOwQ", "pic", "CHANCE:0.15"),
    "износ": ("AgACAgIAAxkBAAIH0Gn-DiyG2LJxYcss4_bDdxOTsqQGAAJSFmsbgn-pS2P1vzmlhqoyAQADAgADeQADOwQ", "pic", "CHANCE:0.15"),
    "рун": ("AgACAgIAAxkBAAIH2Gn-DiwAAXQV9jzpx6xMa1m1-jCojgAC1hNrG_UEuEvafi2ak93sCwEAAwIAA3gAAzsE", "pic", "CHANCE:0.2"),
    "паблик": ("AgACAgEAAxkBAAIHzGn-DiyBqwEw_f2Ah2CrcEYiZVcCAAK7C2sbMlFQR1Serq1-aHivAQADAgADeAADOwQ", "pic", "CHANCE:0.1"),
    "вайб": ("AgACAgIAAxkBAAIHoGn-Bxg8EV_dVCjzfzaU56UX57qFAAJiFmsbzgmgSjxHu4QFuZY4AQADAgADeAADOwQ", "pic", "CHANCE:0.3"),
    "маким": ("AgACAgIAAxkBAAIFOGmoSkG9iHzif-LcBkGEvYBKZq6gAAKxDGsbX5HISz6nimZJVvycAQADAgADeAADOgQ", "pic", "CHANCE:0.3"),
    "растяпа": ("AgACAgIAAxkBAAIFQGmoSnEcPO9V0LTg8IEFKQbwr9TSAAIkDmsbzf8BSHz9iFxyu_oqAQADAgADeQADOgQ", "pic"),
    "аргументация": ("AgACAgIAAx0Cct4JbwABDO0eaagwxIPCoQ-clBEPpHapEA-D3jgAAmYWaxv1AUBJZV0PxkW7p90BAAMCAAN4AAM6BA", "pic", "CHANCE:0.25", "TTL:5"),
    "чилл": ("AgACAgIAAx0Cct4JbwABDOd8aadFMBOIGNI7U-LInFzrlWV0CIEAArASaxugEZhIQeXoXTaKonABAAMCAAN4AAM6BA", "pic", "CHANCE:0.25", "TTL:5"),
    "инсульт": ("AgACAgIAAxkBAAIHxGn-DiyZJvzPJmWEGTM8hC06ccsFAAK_F2sbzZ2oSu1g1sEaBw1vAQADAgADbQADOwQ", "pic", "TTL:5"),
    "канибализм": ("AgACAgIAAxkBAAIHzmn-Diz7oWsxuVFGskC3sRd-8dkGAAJeGmsbr8QxSzaqmjBd9CTNAQADAgADeAADOwQ", "pic", "TTL:5"),
    "король сваг": ("AgACAgIAAx0Cct4JbwABDOvzaaf3r0SL-QXO_2YdTZfXx8f4SYsAAiYTaxv1AUBJvaIDV6yrw4sBAAMCAAN4AAM6BA", "pic", "TTL:5"),
    "отличного сваг": ("AgACAgIAAxkBAAIH0mn-DiwE1GxbNVBOGmWSLebbqntzAAKFE2sbgn-xSwYFf82hY15HAQADAgADeAADOwQ", "pic", "TTL:5"),
    "до связи": ("AgACAgIAAxkBAAIHw2n-Diw-iOXH5BT7XuCcBX1FZGZ3AALdE2sbkkiZSkkNphuzPrkAAQEAAwIAA3gAAzsE", "pic", "TTL:5"),
    "бурятская свага": ("AgACAgIAAxkBAAIHoWn-Bxh7FFQQXqgAAeAsLbhB3oQAAW4AArcUaxuF4LBKVl6e1rUqZucBAAMCAAN4AAM7BA", "pic"),

#————————————————————————————————————————————————————— ОТВЕТЫ ЗВУКАМИ ————————————————————————————————————————————————————————————————————————————————————————————————
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("восстали машины", "восстание машин", "киборг убийца", "киборг-убийца"): ("CQACAgIAAxkBAAIFMGmoSYpmHp53gjn8oKXAg3Q-NrMoAALIhwACJ67YS8NSI3V1y7NyOgQ", "audio"),

#————————————————————————————————————————————————————— ОТВЕТЫ ГОЛОСОВЫМИ —————————————————————————————————————————————————————————————————————————————————————————————    
    #################### ФОРМАТ СПИСОК: СПИСОК
    ("почему", "зачем", "для чего", "нахуя", "схуяли"): (["AwACAgQAAxkBAAIFLGmoSV6j7nc3Fck9jKsv7PJ7C6WNAALfBgAC5ZB1UTE9LfiJGEn5OgQ", "AwACAgIAAx0Cct4JbwABDOabaac_8LU-Y8gUMunYTjopHlb5RlsAAvKfAALsezhJzJPFesXtiRE6BA"], "voice", "NEED_REPLY", "IS_REPLY"),
    
    #################### ФОРМАТ СПИСОК: СТРОКА
    ("делаем грязь", "делай грязь", "делай сука ветер"): ("AwACAgIAAx0Cct4JbwABDO0ZaagvcI4T6JkaqyJyores8XI_hKwAAr2VAAL1AUBJqwm_6OsQcJs6BA", "voice", "IS_REPLY"),
    ("каденза", "каденс", "кейденс"): ("AwACAgIAAxkBAAIFLmmoSXfYsFhJCcFJDU_WHjLpSl0kAAIHlwAC7M4gSG4XNTul_UcuOgQ", "voice", "IS_REPLY", "CHANCE:0.7"),

    #################### ФОРМАТ СТРОКА: СТРОКА
    "почему я яблоко": ("AwACAgIAAxkBAAIHl2n-AS8mrJ0yh7ll1y75DAzuh-6QAAJAXwACnn9oSXDGxiJC_0ghOwQ", "voice", "IS_REPLY")
}