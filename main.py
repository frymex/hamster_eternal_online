import os
import time

from apscheduler.schedulers.background import BackgroundScheduler
from hamster import Hamster

scheduler = BackgroundScheduler()

auth_key = os.environ.get('HAMSTER_API_KEY', '<api_key>')
interval = 1  # в часах

h = Hamster(auth_key=auth_key)

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(h.sync, 'interval', hours=interval)
    scheduler.start()

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
