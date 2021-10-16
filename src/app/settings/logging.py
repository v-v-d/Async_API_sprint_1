import logging

from app.settings import settings

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(funcName)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": "%(levelprefix)s %(client_addr)s - '%(request_line)s' %(status_code)s",
        },
    },
    "handlers": {
        "console": {
            "level": logging.DEBUG,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "uvicorn.access": {
            "level": logging.INFO,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "access",
            "filename": settings.DIR_LOGS / "access.log",
            "maxBytes": 1024 ** 3 * 10,
            "backupCount": 10,
        },
        "uvicorn.error": {
            "level": logging.WARNING,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": settings.DIR_LOGS / "error.log",
            "maxBytes": 1024 ** 3 * 10,
            "backupCount": 10,
        },
        "services": {
            "level": settings.LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": settings.DIR_LOGS / "services.log",
            "maxBytes": 1024 ** 3 * 10,
            "backupCount": 10,
        },
        "services.films": {
            "level": settings.LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": settings.DIR_LOGS / "services.films.log",
            "maxBytes": 1024 ** 3 * 10,
            "backupCount": 10,
        },
        "services.genres": {
            "level": settings.LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": settings.DIR_LOGS / "services.genres.log",
            "maxBytes": 1024 ** 3 * 10,
            "backupCount": 10,
        },
        "services.persons": {
            "level": settings.LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": settings.DIR_LOGS / "services.persons.log",
            "maxBytes": 1024 ** 3 * 10,
            "backupCount": 10,
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["uvicorn.access", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["uvicorn.error", "console"],
            "level": "WARNING",
            "propagate": False,
        },
        "app.services.base": {
            "handlers": ["services", "console"],
            "level": settings.LOG_LEVEL,
            "propagate": False,
        },
        "app.services.films.main": {
            "handlers": ["services.films", "console"],
            "level": settings.LOG_LEVEL,
            "propagate": False,
        },
        "app.services.genres.main": {
            "handlers": ["services.genres", "console"],
            "level": settings.LOG_LEVEL,
            "propagate": False,
        },
        "app.services.persons.main": {
            "handlers": ["services.persons", "console"],
            "level": settings.LOG_LEVEL,
            "propagate": False,
        },
    },
    "root": {
        "level": "INFO",
        "formatter": "verbose",
        "handlers": ["console"],
    },
}
