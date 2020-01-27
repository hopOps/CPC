# SQL Notes

## Postgres

Installation de la lib 

    pip install psycopg2
    
Configuration de postgres in *settings.py*:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432
        }
    }