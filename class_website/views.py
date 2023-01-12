from datetime import datetime
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from product.models import Product

from order.models import Order

from product.forms import ProductForm
from django.views.generic.edit import FormView



# Create your views here.
# READ
class ProductListView(ListView):
    model = Product
    template_name = 'class_website/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['orders'] = Order.objects.all()
        print(context)
        return context


class ProductDetailView(DetailView):
    template_name = 'class_website/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()
    
    def get_object(self):
        obj = super().get_object()
        print(self.kwargs["name"])
        # Record the last accessed date
        obj.last_accessed = datetime.now()
        obj.save()
        return obj



class ContactFormView(FormView):
    template_name = 'class_website/contact.html'
    form_class = ProductForm
    success_url = '/products'

    def form_valid(self, form):
        # form.send_email()
        form.save()
        return super().form_valid(form)





from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'quantity']
    success_url = reverse_lazy('product')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product')
