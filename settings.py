import os


bot_token = '6005280796:AAGz4BI8n5-BpeXqY3dSnx3yi0FRdleQuU0'


standart_delay = 0.5                    # Ппромежуток времени до добавления новой строки
stiker_delay = 0.7                      # сколько висит стикер до удаления
delay_between_stiker_and_message = 0.3  # только после молнии! время между удалением стикера и отправкой сообщения
dice_delay = 3                          # результат после отправки боулинга
guides_delay = 30                       # между отправкой ссылки на статью и "напищи ключевое слово"


answer1 = 'деньги'
answer2 = '3'
answer3 = 'автоворонка'
answer4 = 'масштаб'


res_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res')
audios_path = os.path.join(res_path, 'audios')
audio1 = os.path.join(audios_path, 'audio1.ogg')
audio2 = os.path.join(audios_path, 'audio2.ogg')
audio3 = os.path.join(audios_path, 'audio3.ogg')
