import asyncio

import structlog

from app.utils.updaters import update_asset_total_balance
from app.utils.exceptions import handle_exception
from app.config import BackgroundTasksConfig

logger = structlog.get_logger(__name__)


async def update_asset_total_balance_task():
    while True:
        try:
            logger.info("Updating asset total balance")
            await update_asset_total_balance()
            logger.info("Asset total balance updated successfully")
        except Exception as e:
            logger.error("Error updating asset total balance", error=str(e))
            await handle_exception(e)

        await asyncio.sleep(BackgroundTasksConfig.ASSET_TOTAL_BALANCE_UPDATE_INTERVAL)
