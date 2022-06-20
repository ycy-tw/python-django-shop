from django.urls import path
from .views import (
    product_list,
    product_detail,
    home,
    shop_detail,
    create_product,
    create_shop,
    backend,
    search_view,
    search_result,
    edit_product,
    delete_product,
    edit_shop,
    delete_shop,
    edit_user,
)

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('all', product_list, name='product_list'),
    path('backend', backend, name='backend'),
    path('category/<slug:category_slug>', product_list, name='product_list_by_category'),
    path('user/edit_user', edit_user, name='edit_user'),

    path('product', create_product, name='create_product'),
    path('product/<int:id>/<slug:slug>', product_detail, name='product_detail'),
    path('product/edit/<int:id>/<slug:slug>', edit_product, name='edit_product'),
    path('product/delete/<int:id>/<slug:slug>', delete_product, name='delete_product'),

    path('shop', create_shop, name='create_shop'),
    path('shop/<int:shop_id>', shop_detail, name='shop_detail'),
    path('shop/edit/<int:shop_id>', edit_shop, name='edit_shop'),
    path('shop/delete/<int:shop_id>', delete_shop, name='delete_shop'),

    path('search/', search_view, name='search_view'),
    path('search/<str:keyword>', search_result, name='search_result'),
    path('search/<str:keyword>/<str:condition>', search_result, name='condition_search_result'),
]
