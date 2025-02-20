from decouple import config


class PostgresConfig:
    HOST = config('POSTGRES_HOST', default='localhost')
    PORT = config('POSTGRES_PORT', default=5432)
    DB = config('POSTGRES_DB', default='app')
    USER = config('POSTGRES_USER', default='postgres')
    PASSWORD = config('POSTGRES_PASSWORD', default='postgres')


class RedisConfig:
    HOST = config('REDIS_HOST', default='localhost')
    PORT = config('REDIS_PORT', default=6379)
    DB = config('REDIS_DB', default=0)
    PASSWORD = config('REDIS_PASSWORD', default='redis')


class BybitApiConfig:
    API_KEY = config('BYBIT_API_KEY')
    API_SECRET = config('BYBIT_API_SECRET')


class AppConfig:
    BOT_TOKEN = config('BOT_TOKEN')
    ADMIN_IDS = config('ADMIN_IDS', default='')

    ADMIN_IDS = [int(id) for id in ADMIN_IDS.split(',')]
