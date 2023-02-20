
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('product/<pk>/', views.product),
    # path('add_product_to_cart/<pk>/',views.add_product_to_cart), 
]
