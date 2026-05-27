import logging

import structlog


def configure_logging(*, log_level: str = "INFO", json: bool = False) -> None:
    """Configure structlog so every workspace logs the same way.

    - `json=False` (default): pretty console renderer, great for local dev.
    - `json=True`:            JSON renderer for production, ready to ship to
                              your log aggregator.
    """
    logging.basicConfig(level=log_level, format="%(message)s")
    processors: list[structlog.types.Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
    ]
    processors.append(structlog.processors.JSONRenderer() if json else structlog.dev.ConsoleRenderer())
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(logging.getLevelName(log_level)),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    return structlog.get_logger(name)
