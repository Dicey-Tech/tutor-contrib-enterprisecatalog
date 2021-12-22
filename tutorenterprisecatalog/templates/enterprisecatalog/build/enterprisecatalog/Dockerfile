FROM docker.io/ubuntu:20.04
LABEL maintainer="Sofiane Bebert <s.bebert:diceytech.co.uk>"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y curl git-core language-pack-en python3 python3-pip python3-venv \
    build-essential libffi-dev libmysqlclient-dev libxml2-dev libxslt-dev libjpeg-dev libssl-dev
ENV LC_ALL en_US.UTF-8

ARG ENTERPRISE_CATALOG_REPOSITORY=https://github.com/edx/enterprise-catalog.git 
ARG ENTERPRISE_CATALOG_VERSION={{ OPENEDX_COMMON_VERSION }}

RUN mkdir /openedx
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

# Install django-redis for using redis as a django cache
RUN pip install django-redis==4.12.1

# Install uwsgi
RUN pip install uwsgi==2.0.19.1

{{ patch("enterprisecatalog-dockerfile-post-python-requirements") }}

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD uwsgi \
    --static-map /static=/openedx/enterprise-catalog/enterprise_catalog/assets \
    --http 0.0.0.0:8000 \
    --thunder-lock \
    --single-interpreter \
    --enable-threads \
    --processes=2 \
    --buffer-size=8192 \
    --wsgi-file enterprise_catalog/wsgi.py