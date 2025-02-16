from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Order,CustomUser,Product,Category

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['full_name', 'email', 'address']
        widget={
        
        'full_name': forms.TextInput(attrs={'class':'form_control'}),
        'email': forms.EmailInput(attrs={'class':'form_control'}),
        'address': forms.Textarea(attrs={'class':'form_control'})
        
                 }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if Order.objects.filter(email=email,paid=False).exists():
            raise forms.ValidationError(" Bu e-posta adresi ile ödenmemiş siparişiniz var.")
        return email

class CustomUserCreationForm(UserCreationForm):
    class Meta (UserCreationForm.Meta):
        
           model=CustomUser
           fields=('username','email','password1','password2')

    def clean_email(self):
        email=self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e posta adresi daha önce kaydedilmiştir.")
        
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('username','email','bio','location')

    def clean_email(self):
        email=self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Bu e mail adresi kayıtlıdır.")
        
        return email
class CustomAuthenticationForm (AuthenticationForm):
    usernama=forms.CharField(label='Username',widget=forms.TextInput(attrs={'autofocus':True}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput)


class ProductForms(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','stock','category','description','available','image']
        widgets={
            'description':forms.Textarea(attrs={'rows':4 ,'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'rows':4,'class':'form-control-file'})

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']
        widgets={
            'description':forms.Textarea(attrs={'rows':4,'class':'form-control'})
        }

