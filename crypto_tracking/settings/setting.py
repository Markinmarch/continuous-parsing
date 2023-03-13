'''
Настроечный файл. Реализует подключение к БД,
настройки логгирования, подключение к драйверу.
'''


from redis import StrictRedis
import logging

from crypto_tracking.settings.config import REDIS_HOST as host
from crypto_tracking.settings.config import REDIS_PORT as port
from crypto_tracking.settings.config import REDIS_PASSWORD as pswd


if not port:
    raise ValueError(
        "REDIS_PORT env variables "
        "wasn't implemented in .env (both should be initialized)."
    )

if not pswd:
    raise ValueError(
        "REDIS_PASSWORD env variables "
        "wasn't implemented in .env (both should be initialized)."
    )   

if not host:
    raise ValueError(
        "REDIS_HOST env variables "
        "wasn't implemented in .env (both should be initialized)."
    )

cache = StrictRedis(
    host = host,
    port = port,
    password = None,
    db = 0
)

logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger(__name__)