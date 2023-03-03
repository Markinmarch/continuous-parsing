import os

from dotenv import load_dotenv


load_dotenv()


REDIS_HOST = os.getenv('REDIS_HOST', '')

REDIS_PORT = os.getenv('REDIS_PORT', '')

REDIS_PASSWORD = None

DIFFERENT_PERSENT = 1

HOUR = 3600

URL_PARSE = 'https://www.coingecko.com/en/coins/ethereum'