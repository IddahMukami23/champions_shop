from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add-products/', views.add_products, name='add-products'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update_products, name='delete'),
    path('payments/<id>', views.pay, name='pay'),
]
