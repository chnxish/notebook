# Library

  + [Python](#python)

  + [JavaScript](#javascript)

## python

***

  + bypy

    - Install: pip3 install bypy

    - Upload: bypy upload filename

    - Download: bypy downfile filename

    - Info: bypy list

  + django

    - Install: pip3 install django

    - Create A Project: django-admin startproject project_name

    - Create A App: python3 manage.py startapp app_name

    - Run: python3 manage.py runserver 0.0.0.0:8000

  + django-cors-headers

    - Install: pip3 install django-cors-headers

    - `Add info to settings.py`

```python
INSTALLED_APPS = [
  ...,
  'corsheaders',
  ...,
]

MIDDLEWARE = [
  ...,
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  ...,
]

# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
```

  + django-grappelli

    - Install: pip3 install django-grappelli

    - `Add info to settings.py`

    - `Add code to backend/urls.py`

    - `python3 manage.py collectstatic`

```python
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
)

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]
```

```python
from django.conf.urls import include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
]
```

  + djangorestframework

    - Install: pip3 install djangorestframework

    - `Add info to settings.py`

```python
INSTALLED_APPS = [
  ...,
  'rest_framework',
]
```

  + pymysql

    - Install: pip3 install pymysql

    - `Add code to backend/__init__.py`

```python
import pymysql
pymysql.install_as_MySQLdb()
```

## javascript

***

  + antd

    - Install: npm install --save antd

  + axios

    - Install: npm install --save axios

  + bootstrap

    - Install: npm install --save bootstrap

  + create-react-app

    - Install: npm install -g create-react-app

  + react-router-dom

    - Install: npm install --save react-router-dom
