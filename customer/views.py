from django.shortcuts import render

# Create your views here.

def chom(request):
    return render(request,'customer/customerhome.html')

def clog(request):
    return render(request,'customer/customerlogin.html')

def mycrt(request):
    return render(request,'customer/my_cart.html')

def myorder(request):
    return render(request,'customer/my-orders.html')


def product_detail(request):
    return render(request,'customer/detail.html')
