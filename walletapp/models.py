from django.db import models
from django.db.models.signals import post_save
import qrcode 
from io import BytesIO
from django.core.files import File 
from PIL import Image, ImageDraw

# Create your models here.
class user_field(models.Model):
    email = models.EmailField(max_length=50,blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    otp = models.IntegerField(blank=True,null=True)
    Account_number = models.IntegerField(max_length=50,blank=True,null=True)
    amount = models.IntegerField(max_length=50, null=True, blank=True)
    withdraw = models.IntegerField(blank=True,null=True) 
    add_money = models.IntegerField(blank=True,null=True)
    qr_code = models.ImageField(upload_to = 'qr_code', blank=True)
    profile_image = models.ImageField(upload_to='profileimage', blank=True)
   
    
    def _str_(self) :
        return self.email
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')    
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save = False)
        canvas.close()
        super().save (*args, **kwargs)
    
def create_wallet(sender,instance,created,**kwargs):
    if created:
        user_field.objects.create(user=instance) 
        instance.save()
    post_save.connect(create_wallet,sender=user_field)
