from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename("tutorenterprisecatalog", "templates")

config = {
    "add": {
        "MYSQL_PASSWORD": "{{ 8|random_string }}",
        "SECRET_KEY": "{{ 24|random_string }}",
        "OAUTH2_SECRET": "{{ 8|random_string }}",
        "OAUTH2_SECRET_SSO": "{{ 8|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}diceytech/openedx-enterprise-catalog:{{ ENTERPRISECATALOG_VERSION }}",
        "WORKER_DOCKER_IMAGE": "openedx-enterprise-catalog-worker",
        "HOST": "enterprisecatalog.{{ LMS_HOST }}",
        "MYSQL_DATABASE": "enterprisecatalog",
        "MYSQL_USERNAME": "enterprisecatalog",
        "OAUTH2_KEY": "enterprisecatalog",
        "OAUTH2_KEY_DEV": "enterprisecatalog-dev",
        "OAUTH2_KEY_SSO": "enterprisecatalog-sso",
        "OAUTH2_KEY_SSO_DEV": "enterprisecatalog-sso-dev",
        "CACHE_REDIS_DB": "{{ OPENEDX_CACHE_REDIS_DB }}",
    },
}

hooks = {
    "build-image": {
        "enterprisecatalog": "{{ ENTERPRISECATALOG_DOCKER_IMAGE }}",
        "enterprisecatalog-worker": "{{ ENTERPRISECATALOG_WORKER_DOCKER_IMAGE }}",
    },
    "init": ["mysql", "enterprisecatalog", "lms"],
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename("tutorenterprisecatalog", "patches")
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
