from .environment import env, BASE_DIR

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if env.bool('test'):
    default = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
elif env.str('DB_NAME', default=False):
    default = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
    }
else:  # Local
    default = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

DATABASES = {
    'default': default
}
