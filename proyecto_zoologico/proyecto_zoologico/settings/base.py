
# IMPORTAR EL ARCHIVO (secret.json)
from django.core.exceptions import ImproperlyConfigured
import json


from pathlib import Path
from unipath import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Abrir nuestro archivo (secret.json)
# as f : Agregamos el archivo (secret.json) a la variable f
with open("secret.json") as f:
    # secret : Va obtener los datos que tiene el archivo (secret.json)
    # pero los va a obtener en formato json
    secret = json.loads(f.read())


# Definir una funcion
def get_secret(secret_name, secrets=secret):
    try:
        #
        return secrets[secret_name]
    except:
        msg = "La variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# APLICACION INSTALADAS EN NUESTRO ENTORNO LOCAL
LOCAL_APPS = (
    'applications.users',
    'applications.alimentos',
    'applications.animales',
)


# APLICACION DE TERCEROS
THRID_PARTY_APPS = (
    'rest_framework',
)

#
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THRID_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_zoologico.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_zoologico.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-gt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


