from django import forms
from django.forms import ModelForm
from .models import user_field

class EmployeeForm(ModelForm):
    class Meta:
        model = user_field
        
        fields = ('name', 'email', 'mobile')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobile'}),
        }