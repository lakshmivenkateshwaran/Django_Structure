from django.urls import path
from .views import products
from .views import categories
from .views import get_product

urlpatterns = [
    path('products/', products),
    path('categories/', categories),
    path('products/<int:id>/', get_product)
]