import os
import emoji


bot_token = '6292095984:AAEtTeZSom2dW6uIuEHdOjMWE341Wy5gI0w'
admin_id = 236125284


dynamic_delay = 0.032
dynamic_delay_many = 0.027
standart_delay = 0.6                    # промежуток времени до добавления новой строки
stiker_delay = 1.3                      # сколько висит стикер до удаления
money_stiker_delay = 1.7
delay_between_stiker_and_message = 0.3  # только после молнии! время между удалением стикера и отправкой сообщения
dice_delay = 3                          # результат после отправки боулинга
guides_delay = 10                       # между отправкой ссылки на статью и "напищи ключевое слово"
del_delay = 1                           # после зачёркивания надписи
del_button_delay = 1.3                  # пауза перед удалением кнопки


guide1 = 'https://teletype.in/@money_funnel/VTM9vPZlTJ5'
guide2 = 'https://teletype.in/@money_funnel/za6gUn6kpF2'
guide3 = 'https://teletype.in/@money_funnel/cStvUsIyl8O'


answer1 = 'деньги'
answer2 = ['3', emoji.emojize(":keycap_3:")]
answer3 = 'автоворонка'
answer4 = 'масштаб'


res_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'res')
audios_path = os.path.join(res_path, 'audios')
audio1 = os.path.join(audios_path, 'audio1.ogg')
audio2 = os.path.join(audios_path, 'audio2.ogg')
audio3 = os.path.join(audios_path, 'audio3.ogg')
pdf = os.path.join(res_path, 'pdf.pdf')


progress_emoji_1 = emoji.emojize(":radio_button:")
progress_emoji_2 = emoji.emojize(":white_circle:")
