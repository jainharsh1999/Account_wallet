from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(user_field)
class user_fieldAdmin(admin.ModelAdmin):
    list_display =  ['email', 'name', 'mobile','Account_number','amount', 'withdraw', 'add_money']  

  