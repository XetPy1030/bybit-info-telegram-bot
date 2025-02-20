from datetime import datetime

import pytz

from app.config import AppConfig


def format_dt(dt: datetime) -> str:
    return dt.astimezone(pytz.timezone(AppConfig.TIMEZONE)).strftime('%Y-%m-%d %H:%M:%S')
