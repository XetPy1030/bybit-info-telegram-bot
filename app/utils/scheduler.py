from datetime import timedelta, datetime, timezone

import structlog
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tortoise import BaseDBAsyncClient
from tortoise.signals import post_save

from app.config import BackgroundTasksConfig
from app.database.models import BybitSecretKey
from app.utils.notifiers import notify_about_expired_cookies


logger = structlog.get_logger(__name__)
scheduler = AsyncIOScheduler()


async def schedule_expiration_notifications(secret_key: BybitSecretKey):
    """Schedule notifications for secret key expiration."""
    if not secret_key.expires_at:
        return

    logger.info(
        "Adding notification jobs for secret key",
        secret_key=secret_key.secret_key,
        expires_at=secret_key.expires_at
    )

    now = datetime.now(tz=timezone.utc)

    for minutes in BackgroundTasksConfig.NOTIFY_ABOUT_COOKIES_EXPIRATION_MINUTES:
        notification_time = secret_key.expires_at - timedelta(minutes=minutes)
        
        if notification_time > now:
            scheduler.add_job(
                notify_about_expired_cookies,
                'date',
                run_date=notification_time,
                args=(secret_key, minutes)
            )


async def remove_previous_jobs():
    logger.info("Removing previous scheduler jobs")
    for job in scheduler.get_jobs():
        job.remove()


async def start_scheduler():
    first_key = await BybitSecretKey.get_last()
    if first_key:
        await schedule_expiration_notifications(first_key)

    logger.info("Starting scheduler")
    scheduler.start()
