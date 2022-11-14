from django.db import models

# Create your models here.
class wallet(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    # password = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    otp = models.IntegerField(blank=True,null=True)
    id = models.IntegerField(primary_key= True)
    amount = models.IntegerField(blank=True,null=True)

    
    def _str_(self) :
        return self.email
    
    
    
    
