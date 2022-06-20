from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from cart.forms import CartAddProductForm
from .models import Category, Product, Image, Shop
from .forms import ProductForm, ShopForm, SearchForm
from order.models import Order
from account.forms import UserEditForm
from django.db.models import Q


@login_required
def edit_user(request):

    user = request.user
    form = UserEditForm(instance=user)
    context = {'form': form, 'user': user, 'mode': 'edit'}
    if request.POST:
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('shop:backend')

    return render(request, 'shop/edit_user.html', context)


def search_view(request):
    form = SearchForm()

    if 'query' in request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            return HttpResponseRedirect(
                reverse('shop:search_result', kwargs={'keyword': query})
            )

    else:
        return redirect('shop:home')


@csrf_exempt
def search_result(request, keyword, condition=None):

    products = Product.objects.filter(available=True)
    context = {}

    if condition:

        if condition == 'latest':
            products = products.filter(Q(name__contains=keyword) | Q(description__contains=keyword)) \
                .order_by('-created')

        if condition == 'price':
            products = products.filter(Q(name__contains=keyword) | Q(description__contains=keyword)) \
                .order_by('price')

        context['condition'] = condition

    else:
        products = products.filter(Q(name__contains=keyword) | Q(description__contains=keyword))

    context['keyword'] = keyword
    context['products'] = products

    return render(request, 'shop/search.html', context)


def home(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}

    return render(request, 'shop/home.html', context)


def backend(request):

    user = request.user
    orders = Order.objects.filter(user=user)
    shops = Shop.objects.filter(user=user)
    context = {
        'orders': orders,
        'shops': shops,
        'user': user,
    }

    return render(request, 'shop/backend.html', context)


@login_required
def delete_shop(request, shop_id):

    shop = Shop.objects.get(id=shop_id)

    if request.user != shop.user:
        raise Http404('Invalid action')

    shop.delete()

    return HttpResponseRedirect(reverse('shop:backend'))


@ login_required
def edit_shop(request, shop_id):

    shop = Shop.objects.get(id=shop_id)
    form = ShopForm(instance=shop)
    context = {
        'shop': shop,
        'mode': 'edit',
        'form': form,
    }
    if request.POST:
        form = ShopForm(request.POST,  request.FILES, instance=shop)

        if form.is_valid():

            shop = form.save(commit=False)
            shop.slug = slugify(shop.name)
            shop.save()

            return HttpResponseRedirect(
                reverse(
                    'shop:shop_detail',
                    kwargs={'shop_id': shop.id, }
                )
            )

    return render(request, 'shop/shop/new_shop.html', context)


def shop_detail(request, shop_id):

    shop = Shop.objects.get(id=shop_id)
    products = Product.objects.filter(available=True).filter(shop=shop)
    context = {
        'products': products,
        'shop': shop,
    }

    return render(request, 'shop/shop/detail.html', context)


@ login_required
def create_shop(request):

    form = ShopForm()
    context = {
        'form': ShopForm(),
    }
    if request.POST:
        form = ShopForm(request.POST, request.FILES)

        if form.is_valid():

            shop = form.save(commit=False)
            shop.user = request.user
            shop.slug = slugify(shop.name)
            shop.save()

            return HttpResponseRedirect(
                reverse(
                    'shop:shop_detail',
                    kwargs={'shop_id': shop.id, }
                )
            )

    return render(request, 'shop/shop/new_shop.html', context)


@ login_required
def delete_product(request, id, slug):

    product = Product.objects.get(id=id, slug=slug)
    shop = product.shop

    if request.user != product.shop.user:
        raise Http404('Invalid action')

    product.delete()

    return HttpResponseRedirect(reverse('shop:shop_detail',
                                        kwargs={'shop_id': shop.id, }))


@ login_required
def edit_product(request, id, slug):

    product = Product.objects.get(id=id, slug=slug)
    user = request.user
    form = ProductForm(user, instance=product)
    context = {
        'mode': 'edit',
        'product': product,
        'form': form,
    }
    if request.POST:
        # update existed instance
        form = ProductForm(user, request.POST, instance=product)

        if form.is_valid():

            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()

            images = request.FILES.getlist('image')

            if images:
                for image in images:
                    Image.objects.create(
                        product=product,
                        image=image,
                    )

            return HttpResponseRedirect(
                reverse(
                    'shop:product_detail',
                    kwargs={'id': product.id, 'slug': product.slug}
                )
            )

    return render(request, 'shop/product/new_product.html', context)


@ login_required
def create_product(request):

    user = request.user
    form = ProductForm(user)
    context = {
        'mode': 'new',
        'form': form,
    }
    if request.POST:
        form = ProductForm(user, request.POST)

        if form.is_valid():

            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.save()

            images = request.FILES.getlist('image')
            if images:
                for image in images:
                    Image.objects.create(
                        product=product,
                        image=image,
                    )

            return HttpResponseRedirect(
                reverse(
                    'shop:product_detail',
                    kwargs={'id': product.id, 'slug': product.slug}
                )
            )

    return render(request, 'shop/product/new_product.html', context)


def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):

    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True
    )

    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'shop/product/detail.html', context)
