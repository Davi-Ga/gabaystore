"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from gabaystore import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homePage'),
    
    path('register/',views.register,name='registerPage'),
    path('login/',views.login,name='loginPage'),
    path('logout/',views.logout,name='logoutPage'),
    path('profile/',views.profile,name='profilePage'),
    
    path('store/',views.store,name='storePage'),
    path('cloth_add/',views.clothing_add,name='addClothPage'),
    path('cloth_delete/<int:pk_cloth>',views.clothing_delete,name='deleteClothPage'),
    path('cloth_update/<int:pk_cloth>',views.clothing_update,name='updateClothPage'),
    path('cloth_detail/<int:pk_cloth>',views.clothing_detail,name='detailClothPage'),

]
