"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from walletapp.views import *
from .import views

urlpatterns = [
    path('register', register, name='register'),
    path('login/', login, name='login'),
    path('verify', verify, name='verify'), 
    path('wallet_dashboard/<str:mobile>', wallet_dashboard, name='wallet_dashboard'),
    path('bank_statement/<str:mobile>', bank_statement, name='bank_statement'),
    path('edit/<pk>', update_dashboard, name='edit-employee'),
    path('delete/<pk>', delete_employee, name='delete-employee'),
    path('edit_amount', edit_amount, name='editAmount'),
    path('my_account/<str:mobile>', my_account, name='my_account'),
    path('transfer_money', transfer_money, name='transfer_money'),
    
    
]
