from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from forms import UserRegisterForm

def login(request):
    if request.user.is_authenticated:
        redirect('homePage')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homePage')
            else:
                return #Error mensage
        context={}
        return render(request,'user/login.html',context=context)

def registro(request):
    if request.user.is_authenticated:
        redirect('homePage')
    else:
        form=UserRegisterForm()
        if request.method=='POST':
            form=UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()    
                return redirect('loginPage')
        context={
            'form':form
        }
        return render(request,'user/register.html',context=context)
