from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(wallet)
class walletAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'mobile']
    # list_display = ['email','password', 'name']
    
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ['otp', 'mobile']    