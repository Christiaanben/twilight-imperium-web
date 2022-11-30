from app.settings import env

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{env.str("REDIS_HOST")}:6379',
    }
}
