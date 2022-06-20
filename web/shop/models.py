from django.db import models
from django.urls import reverse
from account.models import Account


class Category(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:

        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category',
            args=[self.slug]
        )


class Shop(models.Model):

    name = models.CharField(max_length=200, unique=True, db_index=True)
    user = models.ForeignKey(Account,
                             related_name='owner',
                             on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.CharField(max_length=200, db_index=True)
    shop_img = models.ImageField(
        null=True,
        upload_to='shop/',
        default='shop/default_shop.jpg'
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:shop_detail',
            args=[self.id, self.slug]
        )


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)

    # user decimal to avoid float rounding issues.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop,
                             related_name='seller',
                             on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[self.id, self.slug]
        )


class Image(models.Model):

    image = models.ImageField(upload_to='product/')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='image',
    )

    def __str__(self):
        return f'{self.product} - {self.id}'
