from django.urls import path
from . import views

app_name = 'reseller'

urlpatterns = [
    path('resellerhome',views.reseller, name='home'),
    path('product_add',views.add_product, name='add_product'),
    path('order',views.myorder, name='order')
    
]