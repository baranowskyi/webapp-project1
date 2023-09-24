from pathlib import Path
import os
from dotenv import load_dotenv
import tzlocal

# for JWT
from datetime import timedelta

# use .env
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') 
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()


# redefine Django User model
AUTH_USER_MODEL = 'users.UserSite'


#---------------- INSTALLED APP -----------------------


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  
]

# installed app
INSTALLED_APPS += [
    'rest_framework',    
    'django_filters',
    'fontawesomefree',
    'corsheaders',
]

# installed app authentication
INSTALLED_APPS += [
    'rest_framework.authtoken',    
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
]

# project app
INSTALLED_APPS += [
    'core',
    'users',
]

#absolute URL generate
INSTALLED_APPS += (
    'django.contrib.sites',
    'absoluteuri',
)
ABSOLUTEURI_PROTOCOL = 'http'
SITE_ID = 1

# documentation app (recomended install after all app install)
INSTALLED_APPS += [
    'drf_spectacular',
]

#-------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication',
    ],

    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


MIDDLEWARE = [        
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'corsheaders.middleware.CorsMiddleware',       
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'webapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),        
        'HOST': os.environ.get('DB_HOST'), 
        'PORT': os.environ.get('DB_PORT'),       
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}


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

# local
LANGUAGE_CODE = 'en-us'
TIME_ZONE = tzlocal.get_localzone_name()
USE_I18N = True
USE_TZ = True



STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# extra static directory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#--------------------- API DOCUMENTATION --------------------------

SPECTACULAR_SETTINGS = {
    'TITLE': 'SCCopy API', 
    'VERSION': '0.0.1', 
    'SERVE_INCLUDE_SCHEMA': False, # exclude endpoint /schema

    'SERVE_PERMISSIONS': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'SERVE_AUTHENTICATION': [
        'rest_framework.authentication.BasicAuthentication',
    ],

    'SWAGGER_UI_SETTINGS': {
        'filter': True, # tag search
        'DeeLinking': True,
        'DisplayOperationId': True,
    },

    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,
}


#----------------------- CORS ------------------------

CORS_ALLOWED_ORIGINS = [    
    'http://localhost:3000',  
    'http://127.0.0.1:3000',  
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',  
    'http://127.0.0.1:3000',  
]

# allow send cookie
CORS_ALLOW_CREDENTIALS = True
# block cookie for JS
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True


CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",    
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",    
    "x-csrftoken",
    "origin",      
)

#------------------------ AUTHENTICATION --------------------

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=10),    
    "SIGNING_KEY": os.environ.get("SECRET_KEY_JWT"),
}

DJOSER = {
    'LOGIN_FIELD': 'email',
}






