from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def  register(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        
        user=wallet(name=name, password=password, email=email)
        user.save()
    return render(request,'register.html')

# def login(request):
#     if request.method =='POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         emp=wallet.objects.filter(Email=email, password=password)
#         print(email)
#         print(password)
        
#         if emp.exists():
#             return HttpResponse("login successfull")
#         else:
#             return HttpResponse("404 error")
        
#     return render(request, 'login.html')