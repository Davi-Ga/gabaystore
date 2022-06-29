from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterUserForm
from .models import Cloth
from .forms import ClothingForm

def home(request):
    Cloth.objects.all()
    return render(request,'gabaystore/home.html')

def profile(request):
    return render(request,'gabaystore/profile.html')

def login(request):
    if request.user.is_authenticated:
       return redirect('homePage')
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

def logout(request):
    logout(request)
    return redirect('homePage')

def register(request):
    if request.user.is_authenticated:
       return redirect('homePage')
    else:
        form=RegisterUserForm()
        if request.method=='POST':
            form=RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()    
                return redirect('loginPage')
        context={
            'form':form
        }
        return render(request,'user/register.html',context=context)

def clothing_add(request):
    form=ClothingForm()
    if request.method=='POST':
        form=ClothingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context={
        'form':form
    }
    return render(request,'gabaystore/cloth_add.html',context=context)

def clothing_delete(request,pk_cloth):
    pk_cloth=int(pk_cloth)
    cloth=Cloth.objects.get(id=pk_cloth)
    cloth.delete()
    
    return redirect('homePage')

def clothing_update(request,pk_cloth):
    pk_cloth=int(pk_cloth)
    cloth=Cloth.objects.get(id=pk_cloth)
    form=ClothingForm(request.POST or None,instance=cloth)
    if request.method=='POST':
        form=ClothingForm(request.POST,request.FILES,instance=cloth)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context={
        'form':form
    }
    return render(request,'gabaystore/cloth_update.html',context=context)

def clothing_detail(request,pk_cloth):
    pk_cloth=int(pk_cloth)
    cloth=Cloth.objects.get(id=pk_cloth)
    context={
        'cloth':cloth
    }
    return render(request,'gabaystore/cloth_detail.html',context=context)