from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
import random
from .forms import EmployeeForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']
        
        user=wallet(name=name, mobile_number=mobile_number, email=email)
        user.save()
    return render(request,'register.html')

def get_otp():
    otp = "" 
    for i in range(4):
        otp += str(random.randint(1,9))
    return otp
    
def login(request):
    if request.method =='POST':
        mobile = request.POST['mobile']
        
        try: 
            mob = Login.objects.get(mobile=mobile)
            
        except:
            Login.objects.create(mobile=mobile)
            mob=Login.objects.get(mobile=mobile)    
            
        OTP=get_otp()
        mob.otp=OTP
        mob.save()
        request.session['mobile']=mobile
        return redirect("verify")
        
    return render(request, 'login.html')

def verify(request):
    mobile = request.session['mobile']
    
    if request.method == "POST":
        otp = request.POST.get('OTP')
        verify = Login.objects.get(mobile=mobile)
        
        if verify.otp == int(otp):
            Login.objects.filter(mobile=mobile)
            print("verify")
            return redirect('register')
        else:
            print("Wrong OTP!")
            
    return render(request,'verify.html')      

def wallet_dashboard(request):
    return render(request, 'wallet.html')

def employees_list(request):
    employee = wallet.objects.all()
    return render(request, 'list.html', {"employees":employee})

def update_dashboard(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-list')
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)

def create_dashboard(request):
    return render(request, 'create.html')

def delete_dashboard(request):
    return render(request, 'delete.html')
