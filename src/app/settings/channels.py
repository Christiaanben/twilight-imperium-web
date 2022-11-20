from app.settings import env

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(env.str('REDIS_HOST'), 6379)],
        },
    },
}
