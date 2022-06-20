from django.contrib import admin
from .models import Category, Product, Image, Shop


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ['image', 'product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'slug', 'price',
        'available', 'created', 'updated',
    ]
    list_filter = ['available', 'created', 'updated', ]

    # 'list_editable' must included in 'list_display'
    list_editable = ['price', 'available']

    # specify fields where the value is automatically
    # set using the value of other fields.
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = [
        'user', 'name', 'created',
    ]
    list_filter = ['created']
    prepopulated_fields = {'slug': ('name', )}
