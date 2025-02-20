import logging
import sys

import structlog

from app import config


def setup_logger():
    logging.basicConfig(
        level=config.AppConfig.LOGGING_LEVEL,
        stream=sys.stdout,
    )
    shared_processors: list[structlog.typing.Processor] = [
        structlog.processors.add_log_level,
        structlog.contextvars.merge_contextvars,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
    ]
    processors: list[structlog.typing.Processor] = [*shared_processors]
    if config.AppConfig.LOGGER_PRETTY_PRINT:
        # Pretty printing when we run in a terminal session.
        # Automatically prints pretty tracebacks when "rich" is installed
        processors.extend(
            [
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.dev.ConsoleRenderer(),
            ],
        )
    else:
        # Print JSON when we run, e.g., in a Docker container.
        # Also print structured tracebacks.
        processors.extend(
            [
                structlog.processors.TimeStamper(),
                structlog.processors.dict_tracebacks,
                # structlog.processors.JSONRenderer(serializer=models.base.orjson_dumps),
                structlog.processors.JSONRenderer(),
            ],
        )
    level_mapping = logging.getLevelNamesMapping()
    level = level_mapping[config.AppConfig.LOGGING_LEVEL]
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(level),
    )
