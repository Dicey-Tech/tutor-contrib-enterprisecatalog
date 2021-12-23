FROM docker.io/ubuntu:20.04
LABEL maintainer="Sofiane Bebert <s.bebert:diceytech.co.uk>"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y curl git-core language-pack-en python3 python3-pip python3-venv \
    build-essential libffi-dev libmysqlclient-dev libxml2-dev libxslt-dev libjpeg-dev libssl-dev
ENV LC_ALL en_US.UTF-8

ARG ENTERPRISE_CATALOG_REPOSITORY=https://github.com/edx/enterprise-catalog.git 
ARG ENTERPRISE_CATALOG_VERSION={{ OPENEDX_COMMON_VERSION }}

ARG APP_USER_ID=1000
RUN useradd --home-dir /openedx --create-home --shell /bin/bash --uid ${APP_USER_ID} app
USER ${APP_USER_ID}

RUN git clone $ENTERPRISE_CATALOG_REPOSITORY --branch $ENTERPRISE_CATALOG_VERSION --depth 1 /openedx/enterprise-catalog
WORKDIR /openedx/enterprise-catalog

# Setup empty yml config file, which is required by production settings
RUN echo "{}" > /openedx/config.yml
ENV ENTERPRISE_CATALOG_CFG /openedx/config.yml

# Install python venv
RUN python3 -m venv ../venv/
ENV PATH="/openedx/venv/bin:$PATH"
RUN pip install pip==20.2.3 setuptools==50.3.0

RUN pip3 install -r requirements/production.txt

{{ patch("enterprisecatalog-worker-dockerfile-post-python-requirements") }}

CMD celery worker --app=enterprise_catalog.celery:app --loglevel=info

