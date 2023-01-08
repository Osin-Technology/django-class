from django.urls import path
from .views import (
    home,
    products,
    delete_product
)

urlpatterns = [
    path('', home ),
    path('products', products, name="product"),
    path('products/delete/<int:id>', delete_product, name="delete_product")
]
