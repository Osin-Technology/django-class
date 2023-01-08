from django.urls import path
from .views import (
    home,
    products
)

urlpatterns = [
    path('', home ),
    path('products', products, name="product")
]
