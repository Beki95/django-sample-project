from decouple import config

DEFAULT_FILE_STORAGE = config(
    'DEFAULT_FILE_STORAGE',
    cast=str,
    default='django.application.files.storage.FileSystemStorage'
)
MEDIA_URL = config(
    'MEDIA_URL',
    cast=str,
    default='media/',
)
MEDIA_ROOT = config(
    'MEDIA_ROOT',
    cast=str,
    default='application/media',
)
