from .base import *

# apps needed for deployment server to work
DEPLOYMENT_APPS = [
    'corsheaders',
    'gunicorn',
    'whitenoise',
]
INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + PROJECT_APPS + DEPLOYMENT_APPS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('debug')

# cloudinary api key
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY': config('API_KEY'),
    'API_SECRET': config('API_SECRET'),
}

# storage settings
STORAGES = {
    "default": {
        "BACKEND": 'cloudinary_storage.storage.MediaCloudinaryStorage'
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"
    },
}

# LOGGING TO betterstack.com

better_stack_token = config('better_stack_token')


LOGGING = {
    "version": 1,
    'disable_existing_loggers': False,
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    'handlers': {
        'logtail': {
            'class': 'logtail.LogtailHandler',
            'source_token': better_stack_token,
        },
    },
    'loggers': {
        "": {
            "handlers": [
                "logtail",
            ],
            "level": "INFO",
        },
    },

}


# PRODUCTION SETTINGS
CSRF_TRUSTED_ORIGINS = ['https://backendguru.up.railway.app']
CORS_ORIGIN_ALLOW_ALL = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

# MEDIA AND STATIC STORAGE
STORAGES = {
 "staticfiles": {
     "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
 },
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
