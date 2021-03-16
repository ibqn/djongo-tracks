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

## Create new data

open up django shell

```shell
python manage.py shell
```

create new data

```python
from tracks.models import Track
track1 = Track(title='track1', description='track1 description', url='https://localhost.com/track1')
track1.save()
# or
track2 = Track.objects.create(title='track2', description='track2 description', url='https://localhost.com/track2')

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
