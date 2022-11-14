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
            return redirect('employees-list')

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
            mob = wallet.objects.get(mobile=mobile)
            
        except:
            wallet.objects.create(mobile=mobile)
            mob=wallet.objects.get(mobile=mobile)    
            
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
        verify = wallet.objects.get(mobile=mobile)
        
        if verify.otp == int(otp):
            wallet.objects.filter(mobile=mobile)
            print("verify")
            return redirect('/wallet_dashboard/'+str(verify.id))
        else:
            print("Wrong OTP!")
            
    return render(request,'verify.html')      

def wallet_dashboard(request, pk):
    user = wallet.objects.get(id=pk)
    return render(request, 'wallet.html', {"user":user})

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

def delete_employee(request):
    return render(request, 'delete.html')



@csrf_protect 
def edit_amount(request):
    
    if request.method=="POST":
        id = request.POST.get('id')
        amount = request.POST.get('amount')
        
        user = wallet.objects.get(id = id)
        useramount = int(user.amount)
        useramount += int(amount)
        
        user.amount = str(useramount)
        user.save()
    
        return HttpResponse("<h1>User</h1>"+user.name+"<br><h1>Amount</h1>"+user.amount)
    
    return render(request, 'add_amount.html')
    
    
