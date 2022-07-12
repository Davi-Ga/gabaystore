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
    
    path('store/',views.store,name='storePage'),
    path('cloth_add/',views.clothing_add,name='addClothPage'),
    path('cloth_delete/<int:pk_cloth>',views.clothing_delete,name='deleteClothPage'),
    path('cloth_update/<int:pk_cloth>',views.clothing_update,name='updateClothPage'),
    path('cloth_detail/<slug:slug>',views.clothing_detail,name='detailClothPage'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings. STATIC_URL,document_root=settings. STATIC_ROOT)
