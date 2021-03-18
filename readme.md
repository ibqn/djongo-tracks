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

define your model, then include your app in settings and make migrations

```shell
python manage.py makemigrations
python manage.py migrate
```

spin up the server

```shell
python manage.py runserver 0:4000
```

## Setup and manage MongoDB

pull `mongo` image

```shell
docker pull mongo
```

start mongo instance

```shell
docker run -it -v mongodata:/data/db -p 27017:27017 --name mongodb -d mongo
```

double check, that it is running

```shell
docker ps
```

check logs if necessary

```shell
docker logs mongodb -f
```

check into container

```shell
docker exec -it mongodb bash
```

connect to mongo, simply by running `mongo`

```shell
mongo -host localhost -port 27017
```

stop or start container

```shell
docker stop mongodb
# or
docker start mongodb
```

If you prefer some gui data visualization, than you can install MongoDB Compass

```shell
sudo dpkg -i ~/Downloads/mongodb-compass_1.26.0_amd64.deb

```

## Create new data from shell

open up django shell

```shell
python manage.py shell
```

create new data

```python
from tracks.models import Track
track1 = Track(title='Track 1', description='Track 1 description', url='https://localhost/track1')
track1.save()
# or
track2 = Track.objects.create(title='Track 2', description='Track 2 description', url='https://localhost/track2')
```

## Dump data from database

export data from app's database

```shell
python manage.py dumpdata --indent 2 tracks > tracks/fixtures/tracks.json
```

## Load data from fixtures into database

Load data based on matching fixture file name `tracks.json`

```shell
python manage.py loaddata tracks
```

## Create superuser from `django` shell

```python
from django.contrib.auth.models import User
user=User.objects.create_user('foo', password='bar')
user.is_superuser=True
user.is_staff=True
user.save()
```

## Create superuser

```shell
python manage.py createsuperuser
```
