from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('',views.chom ),
    path('customer_log/',views.clog ),
    path('my_cart/',views.mycrt, name='cart'),
    path('my_order/',views.myorder, name='order'),
    path('detail/',views.product_detail, name='detail')
]