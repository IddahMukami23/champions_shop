from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add-products/', views.add_products,name='add-products'),
]
