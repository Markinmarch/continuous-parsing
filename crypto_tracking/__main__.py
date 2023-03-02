import asyncio
import time
from redis import StrictRedis


from crypto_tracking.app.comparison import CryptoTracking
from crypto_tracking.app.parser import search_course
from crypto_tracking.app.clean_cache import cleaning_timer
from crypto_tracking.settings.config import REDIS_HOST, REDIS_PORT, URL_PARSE, UPDATE_TIME, HOUR


cache = StrictRedis(
    host = REDIS_HOST,
    port = REDIS_PORT,
    password = None,
    db = 0
)


def main():
    crypto_price = asyncio.run(search_course(URL_PARSE))
    crypto_control = CryptoTracking(
        crypto_price,
        cache
        )
    crypto_control.data_comparison()

        
if __name__ == '__main__':

    timer = time.monotonic() + 20
    while time.monotonic() < timer:
        main()
        time.sleep(2)
    else:
        while True:
            main()
            cleaning_timer(cache)
            time.sleep(2)


