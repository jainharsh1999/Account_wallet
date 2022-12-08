from django.shortcuts import render, HttpResponse
from .models import *
from django.shortcuts import redirect
import random
from .forms import EmployeeForm
from django.views.decorators.csrf import csrf_protect 


# Create your views here.
def register(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def get_otp():
    otp = "" 
    for i in range(4):
        otp += str(random.randint(1,9))
    return otp
    
def login(request):
    if request.method =='POST':
        mobile = request.POST['mobile']
        
        try: 
            data = user_field.objects.get(mobile=mobile)
            # code = data.code
            print("Login successfull") 
        
        except :
            data=user_field.objects.create(mobile=mobile) # django will raise exception in case if number does not exist
       
            data = user_field.objects.get(mobile=mobile)   
            
        OTP=get_otp()
        data.otp=OTP
        data.save()
        request.session['mobile']=mobile
        return redirect("verify")
        
    return render(request, 'login.html')

def verify(request):
    mobile = request.session['mobile']
    
    if request.method == "POST":
        otp = request.POST.get('OTP')
        verify = user_field.objects.get(mobile=mobile)
        
        if verify.otp == int(otp):
            user_field.objects.filter(mobile=mobile)
            print("verify")
            return redirect('wallet_dashboard', mobile)
        else:
            print("Wrong OTP!")
            
    return render(request,'verify.html')      



def employees_list(request): 
    employee = user_field.objects.all()
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

def delete_employee(request):
    return render(request, 'delete.html')



@csrf_protect 
def edit_amount(request, mobile):
    request.session['mobile']=mobile
    
    
    
    if request.method=="POST":
        # mobile = request.POST.get('mobile')
        amount = request.POST['amount']
        data2 = user_field.objects.get(mobile=mobile)
        # user = user.objects.get(mobile = mobile)
        balance=int(data2.amount)
        
        balance += int(amount)
        
        data2.amount = str(balance)
        data2.save()
    
        return redirect('my_account',mobile)
    
    return render(request, 'add_amount.html')
    
    
def wallet_dashboard(request, mobile):
    data1 = user_field.objects.filter(mobile=mobile).first()
    request.session['mobile']=mobile
    return render(request, 'wallet_dashboard.html', { "data1":data1})

def my_account(request,mobile):
    request.session['mobile']=mobile
    data2 = user_field.objects.filter(mobile=mobile).first()  
    return render(request,'my_account.html',{ "data2":data2, })

def transfer_money(request):
    return render(request, 'transfer_money.html')

def bank_statement(request, mobile):
    emp = user_field.objects.get(mobile=mobile)
    request.session['mobile']=mobile
    return render(request, 'bank_statement.html',{"emp":emp})

def myprofile(request, mobile):
    data4 = user_field.objects.filter(mobile=mobile).first()
    request.session['mobile']=mobile
    return render(request, 'my_profile.html', {"data4":data4})