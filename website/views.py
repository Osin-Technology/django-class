from django.shortcuts import render, redirect

# Create your views here.

from product.models import (
    Product,
)


def home(request):
    template_path = 'website/index.html'
    context = {}
    context["username"] = "12C"
    context["last_name"] = "aaa"

    return render(request, template_path, context)


def create_products(product_data=None):
    if product_data:
        # name = product_data["name"]
        # qty = product_data["quantity"]
        # price = product_data["price"]

        # approach 1
        # Product.objects.create(name=name, quantity=qty, price=price)

        # approach 2
        data = product_data.copy().dict()
        data.pop('csrfmiddlewaretoken')
        Product.objects.create(**data)

        # approach 3
        # data = {
        #     "quantity": 12,
        #     "price": 34
        # }
        # Product.objects.create(name=name, **data)



def products(request):
    template_path = 'product/product.html'
    context = {}

    products = Product.objects.filter(price=12)
    context["products"] = products

    if request.method == "POST":
        create_products(request.POST)
        return redirect('product')

    return render(request, template_path, context)