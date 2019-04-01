rssscrapper
===========

Time spent: 5h

# Issued commands

```
django-admin startproject rssscrapper
python3 manage.py startapp api
python3 manage.py makemigrations
```

# How to test

Assuming you have fish shell (`sudo apt install -y fish`).

```
cd rssscapper
python3 manage.py currency usd
python3 manage.py currency usd pln
./run.fish
curl localhost:8000/api/currencies/
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
curl localhost/api/currencies
docker exec -it $did python3 manage.py shell
>>> from api.models import ExchangeRate
>>> ExchangeRate.objects.all()
<QuerySet [<ExchangeRate: EUR -> USD: 1.15>]>
```

# Architecture

Django --> DRF --> list route /api/currencies/
|
--> command to fetch currencies (currency)
