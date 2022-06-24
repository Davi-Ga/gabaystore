from django.shortcuts import redirect, render
from forms import UserRegisterForm

def login(request):
    return render(request,'user/login.html')

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
