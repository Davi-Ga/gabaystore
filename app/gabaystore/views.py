from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import allowed_users,admin_only,unauthenticated_user
from .forms import RegisterUserForm
from .forms import ClothingForm
from .models import Cloth

def home(request):

    return render(request,'gabaystore/home.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = customer.order.get_or_create(customer=customer, paid_status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        
    context={'items':items}
    return render(request,'gabaystore/cart.html',context=context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def profile(request):
    return render(request,'gabaystore/profile.html')

@unauthenticated_user
def loginUser(request):
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

@login_required(login_url='loginPage')
def logoutUser(request):
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
                user=form.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                return redirect('loginPage')
        context={
            'form':form
        }
        return render(request,'user/register.html',context=context)
    
def store(request):
    clothes=Cloth.objects.all()
    context={
        'clothes':clothes
    }
    return render(request,'gabaystore/store.html',context=context)


@login_required(login_url='loginPage')
@admin_only
def clothing_add(request):
    form=ClothingForm()
    if request.method=='POST':
        form=ClothingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addClothPage')
    context={
        'form':form
    }
    return render(request,'gabaystore/cloth_add.html',context=context)


@login_required(login_url='loginPage')
@admin_only
def clothing_delete(request,pk_cloth):
    pk_cloth=int(pk_cloth)
    cloth=Cloth.objects.get(id=pk_cloth)
    cloth.delete()
    return redirect('storePage')


@login_required(login_url='loginPage')
@admin_only
def clothing_update(request,pk_cloth):
    pk_cloth=int(pk_cloth)
    cloth=Cloth.objects.get(id=pk_cloth)
    form=ClothingForm(request.POST or None,instance=cloth)
    if request.method=='POST':
        form=ClothingForm(request.POST,request.FILES,instance=cloth)
        if form.is_valid():
            form.save()
            return redirect('storePage')
    context={
        'form':form
    }
    return render(request,'gabaystore/cloth_add.html',context=context)


def clothing_detail(request,slug=None):
    cloth = None
   # pk_cloth=int(pk_cloth)
    if slug is not None:
        cloth = Cloth.objects.get(slug=slug)
    context={
        'cloth':cloth
    }
    return render(request,'gabaystore/cloth_detail.html',context=context)