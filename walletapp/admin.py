from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(wallet)
class walletAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'mobile', 'amount', 'id']
    # list_display = ['email','password', 'name']
    
  