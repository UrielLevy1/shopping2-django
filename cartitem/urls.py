
from django.urls import path, include
from . import views

urlpatterns = [
    path('cartitems/', views.cartitems),
    path('cartitem/<pk>/', views.cartitem),
]
