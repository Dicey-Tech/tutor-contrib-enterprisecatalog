from enterprise_catalog.settings.utils import get_logger_config
from ..production import *

{% include "enterprisecatalog/apps/settings/partials/common.py" %}

BACKEND_SERVICE_EDX_OAUTH2_KEY = "{{ ENTERPRISECATALOG_OAUTH2_KEY_DEV }}"
BACKEND_SERVICE_EDX_OAUTH2_SECRET = "{{ ENTERPRISECATALOG_OAUTH2_SECRET }}"
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

SOCIAL_AUTH_EDX_OAUTH2_KEY = "{{ ENTERPRISECATALOG_OAUTH2_KEY_SSO_DEV }}"
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "{{ ENTERPRISECATALOG_OAUTH2_SECRET_SSO }}"
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = "http://{{ LMS_HOST }}:8000"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_LOGOUT_URL = SOCIAL_AUTH_EDX_OAUTH2_ISSUER + "/logout"

LMS_BASE_URL = "http://{{ LMS_HOST }}:8000"
DISCOVERY_SERVICE_API_URL = "http://{{ DISCOVERY_HOST }}:8381/api/v1/"

LOGGING = get_logger_config(
    log_dir="/var/log",
    edx_filename="enterprisecatalog_worker.log",
    dev_env=True,
    debug=False,
)




