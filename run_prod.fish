#!/usr/bin/fish

cd rssscrapper
python3 manage.py migrate; and \
python3 manage.py collectstatic --noinput; and \
    env DEBUG=0 \
        SECRET_KEY='p_)8#ffosk_n6mn0x*#faank)-jty80d=&l)!%=4mzci@ojn-e'\
    gunicorn rssscrapper.wsgi --bind 0.0.0.0
