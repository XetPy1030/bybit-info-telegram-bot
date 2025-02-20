from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from app import config

storage = RedisStorage(
    redis=Redis(
        host=config.RedisConfig.HOST,
        port=config.RedisConfig.PORT,
        db=config.RedisConfig.DB,
        password=config.RedisConfig.PASSWORD,
    )
)

bot = Bot(token=config.AppConfig.BOT_TOKEN)
dp = Dispatcher(storage=storage)
