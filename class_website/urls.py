from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ContactFormView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)


urlpatterns = [
    path('product/list', ProductListView.as_view() ),
    path('product/detail/<int:pk>/<slug:name>', ProductDetailView.as_view() ),
    path('product/query', ContactFormView.as_view() ),

      path('product/add/', ProductCreateView.as_view(), name='product-add'),
      path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
      path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    #  path('products', products, name="product"),
    # path('products/delete/<int:id>', delete_product, name="delete_product")
]
