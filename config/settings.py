"""
configプロジェクトのDjango設定。

Django 4.2.17を使用して'django-admin startproject'によって生成されました。

このファイルの詳細については、以下を参照してください
https://docs.djangoproject.com/en/4.2/topics/settings/

設定とその値の完全なリストについては、以下を参照してください
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# プロジェクト内のパスをこのように構築します: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# クイックスタート開発設定 - 本番環境には不適切
# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ を参照してください

# セキュリティ警告: 本番環境で使用するシークレットキーは秘密にしてください!
SECRET_KEY = 'django-insecure-uh$1wfi)as(0f6bxp5rbkskj+*wk6)%vuyk8f72qdd7ggd5ycn'

# セキュリティ警告: 本番環境ではデバッグをオンにしないでください!
DEBUG = True

# 本番環境ではホスト名を指定してください
ALLOWED_HOSTS = ['*']


# アプリケーション定義

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello.apps.HelloConfig',  # helloアプリケーションを追加
    'bbs.apps.BbsConfig',  # bbsアプリケーションを追加
    'django_bootstrap5',  # django-bootstrap5を追加
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # テンプレートディレクトリを追加
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bbs.context_processors.search_form',  # bbsアプリケーションのcontext_processors.pyを追加
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# データベース
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# パスワード検証
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# 国際化
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# 静的ファイル (CSS, JavaScript, 画像)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# デフォルトのプライマリキーのフィールドタイプ
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
