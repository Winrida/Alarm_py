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
