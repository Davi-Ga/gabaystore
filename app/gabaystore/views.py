from http.client import HTTPResponse
from itertools import product
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import allowed_users,admin_only,unauthenticated_user
from .forms import RegisterUserForm
from .forms import ClothingForm
from .models import Cloth
from .models import OrderItem,Order
import json
from django.contrib import messages

def home(request):
    
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer, paid_status=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    context={
        'items':items,
        'order':order,
        'cartItems':cartItems
    }
    return render(request,'gabaystore/home.html',context)
    

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer, paid_status=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    context={
        'items':items, 
        'order':order,
        'cartItems':cartItems
    }
    return render(request,'gabaystore/cart.html',context=context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user
    product = Cloth.objects.get(id=productId)
    
    order,created = Order.objects.get_or_create(customer=customer, paid_status=False)
    
    orderItem,created = OrderItem.objects.get_or_create(order=order,cloth=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        messages.success(request,'Item added to cart')
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        messages.success(request,'Item removed from cart')
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)

@login_required(login_url='loginPage')

def profile(request):
    return render(request,'gabaystore/profile.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def wishlist(request):
    clothes= Cloth.objects.filter(users_wishlist=request.user)
    context={
        "wishlist":clothes
    }
    
    return render(request,'gabaystore/wishlist.html',context=context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def add_wishlist(request,id):
    
    cloth=get_object_or_404(Cloth,id=id)
    
    if cloth.users_wishlist.filter(id=request.user.id).exists():
        cloth.users_wishlist.remove(request.user)
        messages.success(request,'Removed from wishlist')
    else:
        cloth.users_wishlist.add(request.user)
        messages.success(request,'Added to wishlist')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginPage')
@admin_only
def orders(request):
    orders=Order.objects.all()
    context={
        'orders':orders
    }
    return render(request,'gabaystore/orders.html',context=context)

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
                messages.error(request,'username or password not correct')
                return redirect('loginPage')
            
        context={}
        return render(request,'user/login.html',context=context)

@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return redirect('homePage')

@unauthenticated_user
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
    
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer, paid_status=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
    
    clothes=Cloth.objects.all()
    context={
        'clothes':clothes,
        'cartItems':cartItems
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
    
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer, paid_status=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
   # pk_cloth=int(pk_cloth)
    if slug is not None:
        cloth = Cloth.objects.get(slug=slug)
    
    context={
        'items':items,
        'order':order,
        'cartItems':cartItems,
        'cloth':cloth
    }
    return render(request,'gabaystore/cloth_detail.html',context=context)