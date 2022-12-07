import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}][{module}:{lineno}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

logger = logging.getLogger()
