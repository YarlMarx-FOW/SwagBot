################################### ДЛЯ ПОЛУЧЕНИЯ АЙДИ ГИФОК/СТИКЕРОВ ####################################
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
# # Хендлер для голосовух
# @dp.message(F.voice)
# async def get_voice_id(message: types.Message):
#     await message.reply(f"ID Этой голосовухи:\n`{message.voice.file_id}`", parse_mode="MarkdownV2")
###########################################################################################################