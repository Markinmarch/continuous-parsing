'''
Модуль __main__ реализует запуск, отсчёт часа после начала работы 
и автоматическое удаление после истечении часа данных из БД с конца
'''


import asyncio
import time


from crypto_tracking.app.comparison import CryptoTracking
from crypto_tracking.app.parser import search_course
from crypto_tracking.app.clean_cache import cleaning_cache
from crypto_tracking.settings.config import URL_PARSE, HOUR, DIFFERENT_PERSENT
from crypto_tracking.settings.setting import cache
from crypto_tracking.settings.setting import logger


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
    try:
        timer = time.monotonic() + HOUR
        while time.monotonic() < timer:
            main()
        else:
            list_len = len(main())
            while True:
                main()
                if len(main()) > list_len: # если длина списка увеличилась - тогда удаляем, т.к мы собераем только неповторяющиеся данные
                    cleaning_cache(cache)
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())
