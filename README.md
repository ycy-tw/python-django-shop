# docker-django-shop-demo

Online shop which built by Django and construct with uWSGI, Nginx and Docker. It contains enrich functions for e-commerce website like shop, cart.

🔗[Check Live Demo](http://52.207.46.107/)


> **This is a demo purpose project.**


# Techniques

|Part               |Technique|
|-------------------|---------|
|Frontend           |HTML, CSS, jQquery, Bootstrap 5|
|Backend            |Django   |
|Database           |PostgreSQL|
|Deploy             |Nginx, uWSGI, Docker, AWS EC2|
|Version Control    |git      |
|Email Sending      |Celery, Redis|



# Usuage

## Prerequisites
make sure your docker version is at least or greater than
```shell
$ docker version --format '{{.Server.Version}}'
'20.10.14'
```


## Development
Under local circumstance, use `docker-compose-dev.yml` to set up project.
```docker
git clone https://github.com/ycy-tw/docker-django-shop-demo.git
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

Under production scenario, use `docker-compose-prod.yml` to set up project. Environment variables should be managed by `.env`.

Clone project
```
git clone https://github.com/ycy-tw/docker-django-shop-demo.git
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

# References

- [Django 3 By Example: Build powerful and reliable Python web applications from scratch, 3rd Edition](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1838981950/ref=sr_1_5?crid=3GW5HFEDDLFB3&keywords=django&qid=1655733334&sprefix=django%2Caps%2C356&sr=8-5)
- [Deploying Django with Docker Compose](https://www.youtube.com/watch?v=mScd-Pc_pX0&ab_channel=LondonAppDeveloper)
- [docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)



# Screenshots

### home
![](./intro/home.png)

### Product detail
![](./intro/product_detail.png)

### Shop detail
![](./intro/shop_detail.png)

### Cart
![](./intro/cart.png)

### Checkout
![](./intro/checkout.png)

### Product List
![](./intro/product_list.png)

### Product Form
![](./intro/product_form.png)

### Shop Form
![](./intro/shop_form.png)

### Edit user
![](./intro/user_form.png)

### User shop
![](./intro/user_shop.png)

### User order
![](./intro/user_order.png)

### Search
![](./intro/search.png)

### Login
![](./intro/login.png)
