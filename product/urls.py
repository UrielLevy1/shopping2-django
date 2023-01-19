
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('product/<pk>/', views.product),    
]
