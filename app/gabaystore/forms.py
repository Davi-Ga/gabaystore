from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cloth
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={ 
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.FileInput(attrs={'class':'form-control'}),
            'password1':forms.Select(attrs={'class':'form-control'}),
            'password2':forms.Select(attrs={'class':'form-control'}),
            }
        
class ClothingForm(forms.ModelForm):
    class Meta:
        model=Cloth
        fields=['name','picture','size']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'picture':forms.FileInput(attrs={'class':'form-control'}),
            'size':forms.Select(attrs={'class':'form-control'}),
        }