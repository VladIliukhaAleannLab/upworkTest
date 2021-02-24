from django.urls import path

from .views import Ecommerce, ProductsView

urlpatterns = [
    path('', Ecommerce.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
]