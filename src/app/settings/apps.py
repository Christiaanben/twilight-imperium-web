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
    # Health Check
    'health_check',
    'health_check.db',
]

project_apps = [
    'game',
]

INSTALLED_APPS = server_apps + django_apps + third_party_apps + project_apps
