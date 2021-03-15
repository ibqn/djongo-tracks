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

## MongoDB

pull `mongo` image

```shell
docker pull mongo
```

start mongo instance

```shell
docker run -it -v mongodata:/data/db --name mongodb -d mongo
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
