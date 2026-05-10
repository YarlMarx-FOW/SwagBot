"""
Из этого файла только копируется необходимый хендлер в handlers.py
Сами эти хендлеры это временный инструментарий, который необходим только при обновлении triggers.py
Потому здесь нет importов, и эти строки должны всегда оставаться комментариями
"""

################################### ДЛЯ ПОЛУЧЕНИЯ АЙДИ ГИФОК/СТИКЕРОВ ####################################
# # Хендлер для стикеров 
# @router.message(F.sticker)
# async def get_sticker_id(message: types.Message):
#     await message.reply(f"ID этого стикера:\n`{message.sticker.file_id}`", parse_mode="MarkdownV2")
# #
# # Хендлер для гифок
# @router.message(F.animation)
# async def get_gif_id(message: types.Message):
#     await message.reply(f"ID этой гифки:\n`{message.animation.file_id}`", parse_mode="MarkdownV2")
# #
# # Хендлер для картинок
# @router.message(F.photo)
# async def get_image_id(message: types.Message):
#     await message.reply(f"ID этой картинки:\n`{message.photo[-1].file_id}`", parse_mode="MarkdownV2") 
# #
# # Хендлер для видев
# @router.message(F.video)
# async def get_video_id(message: types.Message):
#     await message.reply(f"ID этого видоса:\n`{message.video.file_id}`", parse_mode="MarkdownV2")
# #
# # Хендлер для аудиов
# @router.message(F.audio)
# async def get_audio_id(message: types.Message):
#     await message.reply(f"ID этого аудио:\n`{message.audio.file_id}`", parse_mode="MarkdownV2")
# # Хендлер для голосовух
# @router.message(F.voice)
# async def get_voice_id(message: types.Message):
#     await message.reply(f"ID Этой голосовухи:\n`{message.voice.file_id}`", parse_mode="MarkdownV2")
###########################################################################################################