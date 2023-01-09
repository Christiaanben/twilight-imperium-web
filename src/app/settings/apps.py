server_apps = [
    "daphne",
]

django_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

third_party_apps = [
    'rest_framework',
    'channels',
    'corsheaders',
    'django_extensions',
    # Health Check
    'health_check',
    'health_check.db',
    'health_check.contrib.migrations',
    'health_check.cache',
]

auth_apps = [
    'rest_framework.authtoken',
]

project_apps = [
    'game',
    'user',
]

INSTALLED_APPS = server_apps + django_apps + third_party_apps + auth_apps + project_apps
