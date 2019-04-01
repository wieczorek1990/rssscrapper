rssscrapper
===========

Currencies scrapper challenge.

Time spent: 6h

# How to test

Assuming you have fish shell and httpie installed.
If not: `sudo apt install -y fish httpie`.

```
cd rssscapper
python3 manage.py currency usd
python3 manage.py currency usd pln
./run.fish
http --follow localhost:8000/api/currencies/
python3 manage.py shell
>>> from api.models import ExchangeRate
>>> ExchangeRate.objects.all()
<QuerySet [<ExchangeRate: EUR -> USD: 1.15>]>
```

or use Docker:

```
docker-compose up
set did (docker ps | grep rssscrapper_django | tr -s ' ' | cut -f 1 -d ' ')
docker exec -it $did python3 rssscrapper/manage.py currency usd
docker exec -it $did python3 rssscrapper/manage.py currency usd pln
http --follow localhost/api/currencies/
docker exec -it $did python3 manage.py shell
>>> from api.models import ExchangeRate
>>> ExchangeRate.objects.all()
<QuerySet [<ExchangeRate: EUR -> USD: 1.15>]>
```

# Architecture

Django --> DRF --> list route /api/currencies/
|
--> command to fetch currencies (currency)

# Issued commands

```
django-admin startproject rssscrapper
python3 manage.py startapp api
python3 manage.py makemigrations
python3 manage.py createsuperuser
```

