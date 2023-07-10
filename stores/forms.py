from django import forms
from .models import Order, Contacts



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        #fields= ['']
        exclude = ['cart', 'amount', 'order_status', 'discount', 'subtotal', 'payment_complete', 'ref']

        widgets= {
            'order_by': forms.TextInput(attrs={'class': 'form-control'}),
            'shipping_address': forms.Textarea(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
             
        }


class ConForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['First_Name', 'Last_Name', 'Mobile', 'Email', 'Subject', 'Message', ]

        widgets= {

            'First_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ENTER'}),
            'Last_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ENTER'}),
            'Mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ENTER'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ENTER'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ENTER'}),
            'Message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ENTER'}),
            # 'Date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}), 

        }