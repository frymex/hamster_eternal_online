import time

from hamster import Hamster


def auto_tap(auth_key: str, timeout: int = 15, count: int = 15):
    """Фукнция будует нажимать каждые <timeout> секунд

    auth_key: str (requided) auth key for hamster
    timeout: int (default 15) time in seconds
    count: int (default 15) count of hamster to tap
    """

    while True:
        time.sleep(timeout)

        with Hamster(auth_key=auth_key) as h:
            r = h.tap(count=count)
            if isinstance(r, dict):
                print('Ошибка:', r.get('error'))

            print(f'Нажал {count} раз')
