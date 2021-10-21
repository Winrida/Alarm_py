from playsound import *
from datetime import *


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


while True:
    alarm_time = input('Введите время в следующем формате: \'HH:MM:SS\' \nВремя будильника: ')
    validate = validate_time(alarm_time)
    if validate != 'Отлично!':
        print(validate)
    else:
        print(f"Будильник установлен на время{alarm_time}...")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second
