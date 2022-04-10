from Fusion.settings.common import *

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '172.27.16.218', 'fusion.iiitdmj.ac.in']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# password of sender
EMAIL_HOST_PASSWORD = os.environ['MAIL_PASSWORD']

# Database template for postgres

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fusionlab2',
        'HOST': 'localhost',
        'USER': 'fusion_admin',
        'PASSWORD': 'hello123',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
