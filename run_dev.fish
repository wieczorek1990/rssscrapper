#!/usr/bin/fish

cd rssscrapper
python3 manage.py migrate; and \
    env DEBUG=1 SECRET_KEY=secret python3 manage.py runserver
