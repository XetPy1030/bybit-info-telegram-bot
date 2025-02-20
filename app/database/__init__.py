import structlog
from tortoise import Tortoise

from app.database.config import TORTOISE_ORM

logger = structlog.get_logger(__name__)


async def init():
    await Tortoise.init(TORTOISE_ORM)
    # Генерируем схемы
    await Tortoise.generate_schemas()
    logger.info('Database initialized')
