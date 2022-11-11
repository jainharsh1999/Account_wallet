from django import forms
from django.forms import ModelForm
from .models import wallet

class EmployeeForm(ModelForm):
    class Meta:
        model = wallet
        
        fields = ('name', 'email', 'mobile')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobile'}),
        }