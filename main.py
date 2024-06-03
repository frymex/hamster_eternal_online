import os
import time

from apscheduler.schedulers.background import BackgroundScheduler
from utils.printer import print_cazqev

from config import auth_key, interval
from hamster import Hamster


scheduler = BackgroundScheduler()
h = Hamster(auth_key=auth_key)

if __name__ == '__main__':
    print_cazqev()

    scheduler = BackgroundScheduler()
    scheduler.add_job(h.sync, 'interval', hours=interval)
    scheduler.start()

    try:
        connected_status = h.is_connected()
    except UnicodeEncodeError:
        connected_status = False

    if bool(connected_status) is False:
        print('~ Не удалось подключиться к Hamster Kombat. Проверьте токен')
        exit(2)

    print('~ Скрипт успешно запущен. Чтобы его остановить нажми Ctrl+C')
    print(f'~ Выполнен вход под уч. записью: {connected_status.telegramUser.firstName}')

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
