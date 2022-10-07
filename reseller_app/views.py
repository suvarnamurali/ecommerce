from django.shortcuts import render

# Create your views here.

def reseller(request):
    return render(request,'reseller_app/reseller_home.html')

def add_product(request):
    return render(request,'reseller_app/add_product.html')

def myorder(request):
    return render(request,'reseller_app/my_orders.html')

 


