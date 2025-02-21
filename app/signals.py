from tortoise import BaseDBAsyncClient
from tortoise.signals import post_save

from app.database.models import BybitSecretKey
from app.utils.scheduler import remove_previous_jobs, schedule_expiration_notifications

import structlog

logger = structlog.get_logger(__name__)


@post_save(BybitSecretKey)
async def on_bybit_secret_key_save(
    sender: type[BybitSecretKey],
    instance: BybitSecretKey,
    created: bool,
    using_db: BaseDBAsyncClient | None,
    update_fields: list[str],
):
    if created:
        await remove_previous_jobs()
        await schedule_expiration_notifications(instance)


logger.info("Signal registered")
