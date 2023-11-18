import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# psycopg2
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbmaca',
        'HOST': 'localhost',
        'USER': 'maca',
        'PASSWORD': '123',
        'PORT': '5433',
    }
}