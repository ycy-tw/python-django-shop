import os

commands = [
    'python manage.py loaddata fixtures/Account.json --app account.Account',
    'python manage.py loaddata fixtures/Shop.json --app shop.Shop',
    'python manage.py loaddata fixtures/Category.json --app shop.Category',
    'python manage.py loaddata fixtures/Product.json --app shop.Product',
    'python manage.py loaddata fixtures/Image.json --app shop.Image',
    'python manage.py loaddata fixtures/Order.json --app order.Order',
    'python manage.py loaddata fixtures/OrderItem.json --app order.OrderItem',
]

for command in commands:
    os.system(command)

print('Load data done.')
