import asyncio
import structlog

from app.background_tasks.bybit import update_asset_total_balance_task

logger = structlog.get_logger(__name__)


async def run_background_tasks():
    logger.info("Starting background tasks")
    asyncio.create_task(
        update_asset_total_balance_task()
    )
    logger.info("Background tasks started successfully")
