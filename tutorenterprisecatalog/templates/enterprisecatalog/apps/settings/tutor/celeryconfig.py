from enterprise_catalog.settings.utils import get_logger_config
from ..production import *

{% include "enterprisecatalog/apps/settings/partials/common.py" %}

# Logging: get rid of local handler
LOGGING["handlers"].pop("local")

LOGGING = get_logger_config(
    log_dir="/var/log",
    edx_filename="enterprisecatalog_worker.log",
    dev_env=True,
    debug=False,
)




