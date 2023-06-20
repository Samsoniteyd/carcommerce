import datetime
from django import forms
from .models import Order


class RegForm(forms.ModelForm):
    class Meta:
        model = Order

        email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        
        fields=['surname', 'firstname', 'middlename','address', 'email', 'phone', 'date_of_birth', 'booking', 'returnbooking','payment_method']
        widgets ={
            'surname':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SURNAME'}),
            'firstname':forms.TextInput(attrs={'class': 'form-control','placeholder': 'FIRSTNAME'}),
            'middlename':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'booking':forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'returnbooking':forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            # 'total_days':forms.DateInput(attrs={'class': 'form-control','type':'hidden'}),
            # 'amount':forms.DateInput(attrs={'class': 'form-control','type':'hidden'}),
            'payment_method': forms.Select(attrs={'class':'form-control'}),

        }
