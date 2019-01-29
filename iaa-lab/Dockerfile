###################################
#
# IAA Docker Container
# @author Matt Hale
#
###################################

# Pull base image.
FROM python:3.7.2
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image
ENV APP_ROOT /var/www
RUN mkdir /var/www;

WORKDIR ${APP_ROOT}

#Python packages
RUN pip install Django==2.1.5
RUN pip install djangorestframework==3.9.1
RUN pip install psycopg2-binary
