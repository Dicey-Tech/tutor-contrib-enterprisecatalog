SECRET_KEY = "{{ ENTERPRISECATALOG_SECRET_KEY }}"
ALLOWED_HOSTS = [
    "enterprisecatalog",
    "{{ ENTERPRISECATALOG_HOST }}",
    "{{ LMS_HOST }}",
]

PLATFORM_NAME = "{{ PLATFORM_NAME }}"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "{{ ENTERPRISECATALOG_MYSQL_DATABASE }}",
        "USER": "{{ ENTERPRISECATALOG_MYSQL_USERNAME }}",
        "PASSWORD": "{{ ENTERPRISECATALOG_MYSQL_PASSWORD }}",
        "HOST": "{{ MYSQL_HOST }}",
        "PORT": "{{ MYSQL_PORT }}",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "KEY_PREFIX": "enterprisecatalog",
        "LOCATION": "redis://{% if REDIS_USERNAME and REDIS_PASSWORD %}{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}{% endif %}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ ENTERPRISECATALOG_CACHE_REDIS_DB }}",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "{{ SMTP_HOST }}"
EMAIL_PORT = "{{ SMTP_PORT }}"
EMAIL_HOST_USER = "{{ SMTP_USERNAME }}"
EMAIL_HOST_PASSWORD = "{{ SMTP_PASSWORD }}"
EMAIL_USE_TLS = {{ SMTP_USE_TLS }}

LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": "/var/log/enterprisecatalog.log",
    "formatter": "standard",
}
LOGGING["loggers"]["algoliasearch_django"] = {"level": "WARNING"}

# Generic OAuth2 variables irrespective of SSO/backend service key types.
OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

OAUTH_API_TIMEOUT = 5
{% set jwt_rsa_key = rsa_import_key(JWT_RSA_PRIVATE_KEY) %}
import json
JWT_AUTH["JWT_ISSUER"] = "{{ JWT_COMMON_ISSUER }}"
JWT_AUTH["JWT_AUDIENCE"] = "{{ JWT_COMMON_AUDIENCE }}"
JWT_AUTH["JWT_SECRET_KEY"] = "{{ JWT_COMMON_SECRET_KEY }}"

JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "{{ jwt_rsa_key.e|long_to_base64 }}",
                "n": "{{ jwt_rsa_key.n|long_to_base64 }}",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "{{ JWT_COMMON_ISSUER }}",
        "AUDIENCE": "{{ JWT_COMMON_AUDIENCE }}",
        "SECRET_KEY": "{{ OPENEDX_SECRET_KEY }}"
    }
]

EDX_DRF_EXTENSIONS = {
    'OAUTH2_USER_INFO_URL': '{% if ENABLE_HTTPS %}https{% else %}http{% endif %}://{{ LMS_HOST }}/oauth2/user_info',
}

{{ patch("enterprisecatalog-common-settings") }}