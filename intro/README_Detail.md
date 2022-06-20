# docker-django-shop-demo

Online shop project which built by Django framework. It contains complete function for e-commerce website like shop, cart. Construct with uWSGI, Nginx and Docker.

[Live Demo]('http://ec2-54-175-176-63.compute-1.amazonaws.com/)


## Structure

|Structure          |Technique|
|-------------------|---------|
|Frontend           |HTML, CSS, jQquery, Bootstrap 5|
|Backend            |Django   |
|Database           |PostgreSQL|
|Deploy             |Nginx, uWSGI, Docker, AWS EC2|
|Version Control    |git      |
|Email Sending      |Celery, Redis|




# Usuage

## Prerequisites
make sure your docker version is at least or greater than.
```shell
$ docker version --format '{{.Server.Version}}'
'20.10.14'
```


## Development
Under local circumstance, use `docker-compose.dev.yml` to set up project.
```docker
git clone
cd docker-django-shop-demo
docker-compose -f docker-compose-dev.yml up -d
docker-compose -f docker-compose-dev.yml exec web python load_data.py
```

Visit http://127.0.0.1/, login with accounts below to try out.

|email            |password    |level|
|-----------------|------------|-----|
|user1@example.com|testing12345|-    |
|admin@example.com|testing12345|admin|


## Production

Under production scenario, use `docker-compose.prod.yml` to set up project. Environment variables should be managed by `.env`.

Clone project
```
git clone
cd docker-django-shop-demo
```

Setup environment variables
```
touch .env
vi .env
```

Project live
```docker
docker-compose -f docker-compose-prod.yml build
docker-compose -f docker-compose-prod.yml up -d
docker-compose -f docker-compose-prod.yml exec web python load_data.py
```