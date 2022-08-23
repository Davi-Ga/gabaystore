from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cloth
from .models import Shipping
from django import forms

class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={
            'username':None,
            'password1':None,
            'password2':None,
        }
        
class ClothingForm(forms.ModelForm):
    class Meta:
        model=Cloth
        fields=['name','picture','size','clothing_type','price','amount']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'picture':forms.FileInput(attrs={'class':'form-control'}),
            'size':forms.Select(attrs={'class':'form-control'}),
        }

class ShippingForm(forms.ModelForm):
    class Meta:
        model=Shipping
        fields=['address','city','state','zipcode']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.TextInput(attrs={'class':'form-control'}),
        }