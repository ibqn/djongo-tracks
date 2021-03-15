

## Getting started

create a virtual environment
```shell
python3 -m venv './venv'
```
activate it

```shell
source venv/bin/activate.fish
```
initialize a poetry project

```shell
poetry init
```

install `django` and hte latest version of `djongo` as well as `graphene-django`  

```shell
poetry add django
poetry add git+ssh://git@github.com:nesdis/djongo.git
poetry add graphene-django
```

create a django project with 

```shell
django-admin startproject app .
```

create a new `tracks` app

```shell
python manage.py startapp tracks
```