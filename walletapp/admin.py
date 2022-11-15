from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(user_field)
class user_fieldAdmin(admin.ModelAdmin):
    list_display =  ['email', 'name', 'mobile','id']  

@admin.register(wallet_payment)
class wallet_paymentAdmin(admin.ModelAdmin):
    list_display = ['amount', 'withdraw', 'add_money']   