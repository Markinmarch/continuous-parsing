'''
Модуль __main__ реализует запуск, отсчёт часа после начала работы 
и автоматическое удаление после истечении часа данных из БД с конца
'''


import asyncio
import time
from redis import StrictRedis


from crypto_tracking.app.comparison import CryptoTracking
from crypto_tracking.app.parser import search_course
from crypto_tracking.app.clean_cache import cleaning_cache
from crypto_tracking.settings.config import REDIS_HOST, REDIS_PORT, URL_PARSE, HOUR, DIFFERENT_PERSENT


if not REDIS_HOST or not REDIS_PORT:
    raise ValueError(
        "REDIS_HOST and REDIS_PORT env variables "
        "wasn't implemented in .env (both should be initialized)."
    )


cache = StrictRedis(
    host = REDIS_HOST, #localhost
    port = REDIS_PORT, #6379
    password = None,
    db = 0
)


def main():
    crypto_price = asyncio.run(search_course(URL_PARSE))
    crypto_control = CryptoTracking(
        DIFFERENT_PERSENT,
        crypto_price,
        cache
        )
    crypto_control.data_comparison()
    return crypto_control.data_comparison()

        
if __name__ == '__main__':

    timer = time.monotonic() + HOUR
    while time.monotonic() < timer:
        main()
    else:
        list_len = len(main())
        while True:
            main()
            if len(main()) > list_len: # если длина списка увеличилась - тогда удаляем, т.к мы собераем только неповторяющиеся данные
                cleaning_cache(cache)
