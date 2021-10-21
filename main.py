from datetime import *
import pyglet
from threading import Thread


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Неверный формат, попробуйте ещё раз.'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Неверный формат часов, попробуйте ещё раз.'
        elif int(alarm_time[3:5]) > 59:
            return 'Неверный формат минут, попробуйте ещё раз.'
        elif int(alarm_time[6:8]) > 59:
            return 'Неверный формат секунд, попробуйте ещё раз.'
        else:
            return 'Отлично!'


def validate_melody(melody):
    if melody < 1 or melody > 4:
        return 'Выберете мелодию из списка.'
    else:
        return 'Отлично!'


def audio(files):
    media = pyglet.media.load(files)
    media.play()
    pyglet.app.run()


while True:
    alarm_time = input('Введите время в следующем формате: \'HH:MM:SS\' \nВремя будильника: ')
    validate = validate_time(alarm_time)
    if validate != 'Отлично!':
        print(validate)
    else:
        melody = int(input('Выберете номер мелодии: \n1. Лунная Соната - Бетховен\n2. Avicii - Wake Me Up\n3. '
                           'Illenium ft. '
                           'Annika Wells - Crawl outta love \n4. Little Richard - Long Tall Sally\nНомер мелодии: '))
        validate_m = validate_melody(melody)
        if validate_m != 'Отлично!':
            print(validate_m)
        else:
            print(f"Будильник установлен на время: {alarm_time}...")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print('Просыпайся!')
                if melody == 1:
                    player = Thread(target=audio, args=("Лунная Соната - Бетховен.mp3",))
                    player.start()
                elif melody == 2:
                    player = Thread(target=audio, args=("Avicii - Wake Me Up.mp3",))
                    player.start()
                elif melody == 3:
                    player = Thread(target=audio, args=("Illenium ft. Annika Wells - Crawl outta love.mp3",))
                    player.start()
                elif melody == 4:
                    player = Thread(target=audio, args=("Little Richard - Long Tall Sally.mp3",))
                    player.start()
                break
