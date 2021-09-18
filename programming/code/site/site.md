# Site

  + ![React-Django](./resources/react_django.png)

  + folder structure

```
/site
  /backend
    /api
    /backend
  /frontend
```

  + Install the required frameworks and libraries

  + home_page: src/index/index.html

## Django

  + `/site/backend/backend/settings.py`

  + `/site/backend/backend/__init__.py`

  + `/site/backend/backend/wsgi.py`

```python
import os

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
  ...,
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  ...,
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbforpy',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    ('image', os.path.join(STATIC_ROOT, 'image').replace('\\', '/')),
    ('css',  os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js',  os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
```

```python
import pymysql
pymysql.install_as_MySQLdb()
```

```python
import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/site/backend')

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

application = get_wsgi_application()
```

## Apache

  + `/etc/apache2/apache2.conf`

  + `/etc/apache2/mods-available/mod_wsgi.load`

  + `/etc/apache2/ports.conf`

  + `/etc/apache2/sites-available/000-default.conf`

```
ServerRoot "/etc/apache2"
ServerName localhost:8000

<Directory />
    Options FollowSymLinks
    AllowOverride None
    Require all denied
</Directory>

<Directory /usr/share>
    AllowOverride None
    Require all granted
</Directory>

<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

<Directory /var/www/html>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
```

```
LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
```

```
Listen 8000
```

```
<VirtualHost *:8000>
    ServerAdmin webmaster@localhost
    DocumentRoot /site/backend
    # ServerName localhost:8000
    ServerAlias *.chnxish.com

    Alias /static /site/backend/static
    <Directory /site/backend/static>
        Require all granted
    </Directory>

    Alias /media /site/backend/media
    <Directory /site/backend/media>
        Require all granted
    </Directory>

    <Directory /site/backend/backend>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    <Directory /site/backend>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    # WSGIDaemonProcess backend python-home=/root/virtualenvs/website python-path=/site/backend
    # WSGIProcessGroup backend 
    WSGIScriptAlias / /site/backend/backend/wsgi.py

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

## Backend Testing

  + source code: src/django/

  + postman ip:8000/api/hello

## React

## Nginx

## Frontend Testing

