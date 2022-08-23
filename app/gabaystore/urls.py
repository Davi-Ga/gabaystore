from django.conf import settings
from gabaystore import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='homePage'),
    
    path('register/',views.register,name='registerPage'),
    path('login/',views.loginUser,name='loginPage'),
    path('logout/',views.logoutUser,name='logoutPage'),
    path('profile/',views.profile,name='profilePage'),
    
    path('cart/',views.cart,name='cartPage'),
    path('store/',views.store,name='storePage'),
    path('order_detail/<int:id>',views.order_detail,name='orderDetailPage'),
    path('orders/',views.orders,name='ordersPage'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('cloth_add/',views.clothing_add,name='addClothPage'),
    path('wishlist/',views.wishlist,name='wishlistPage'),
    path('wishlist/add/<int:id>',views.add_wishlist,name='addWishlistPage'),
    path('cloth_delete/<int:pk_cloth>',views.clothing_delete,name='deleteClothPage'),
    path('cloth_update/<int:pk_cloth>',views.clothing_update,name='updateClothPage'),
    path('cloth_detail/<slug:slug>',views.clothing_detail,name='detailClothPage'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


