from environ import Env

from config.settings import BASE_DIR

env = Env()

env.read_env('.env')

ALLOWED_HOSTS = env('ALLOWED_HOSTS', list)

CORS_ALLOWED_ORIGINS = env('CORS_ALLOWED_ORIGINS', list)
CORS_ALLOWED_ORIGIN_REGEXES = env('CORS_ALLOWED_ORIGIN_REGEXES', list)

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_USE_SSL = env('EMAIL_USE_SSL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': env('DJANGO_LOG_LEVEL', cast=str,default='INFO'),
            'propagate': False,
        },
    },
}
