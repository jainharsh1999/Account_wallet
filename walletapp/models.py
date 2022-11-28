from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class user_field(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    otp = models.IntegerField(blank=True,null=True)
    Account_number = models.IntegerField(max_length=50,blank=True,null=True)
    
    
class wallet_payment(models.Model):
    amount = models.IntegerField( null=True, blank=True)
    withdraw = models.IntegerField(blank=True,null=True)
    add_money = models.IntegerField(blank=True,null=True)
        
    
    def _str_(self) :
        return self.email
    
def create_wallet(sender,instance,created,**kwargs):
    if created:
        user_field.objects.create(user=instance) 
        instance.save()
    post_save.connect(create_wallet,sender=user_field)
