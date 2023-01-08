from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from product.models import (
    Product,
)

from product.forms import (
    ProductForm,
    ProductCustomForm
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

    form = ProductForm()
    context["form"] = form

    products = Product.objects.all()
    context["products"] = products

    if request.method == "POST":
        if 'post' in request.POST:
            # create_products(request.POST)
            form_data = ProductForm(request.POST)
            if form_data.is_valid():
                print("validated")
                # approach 1
                # Product.objects.create(**form_data.cleaned_data)
                
                # approach 2 for model forms
                form_data.save()
            else:
                print("not validated")

        elif 'update' in request.POST:
            name = request.POST["name"]
            
            # Product.objects.update(**data)
            cur_product = Product.objects.get(name=name)
            cur_product.name = request.POST["name"]
            cur_product.price = request.POST["price"]
            cur_product.quantity = request.POST["quantity"]
            cur_product.save()
            
        else:
            product_id = request.POST["product_id"]
            data = Product.objects.get(id=product_id)
            print(data)

            # products = Product.objects.all()
            # context["products"] = products

            form = ProductForm(instance=data)
            context["form"] = form

            return render(request, template_path, context)


        return redirect('product')

    return render(request, template_path, context)


def delete_product(request, id):
    current_product = Product.objects.filter(id=id).exists()
    if current_product:
        Product.objects.get(id=id).delete()
        return redirect('product')
    else:
        return HttpResponse("no such product")