from datetime import datetime
last_sender_id = None                # Айди того, кто отправил послание через бота
last_response_time = datetime.now()  # Глобальное время последнего ответа бота
PHRASE_TRIGGERS = []