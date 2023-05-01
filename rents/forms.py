from django import forms
from . models import Order




class DateInput(forms.DateInput):
    input_type = 'date'



class RentForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Order
        fields= ['Firstname', 'Secondname', 'mobile', 'email', 'address', 'date_of_booking', 'date_of_return', 'total_days', 'total_amount', 'payment_method']

        widgets = {
            'Firstname':forms.TextInput(attrs={'class':'form-control'}),
            'Secondname':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'date_of_booking': DateInput(),
            'date_of_return':DateInput(),
            'total_days': forms.TextInput(),
            'total_amount': forms.TextInput(),
            'Payment_method':forms.Select(attrs={'class':'form-control'})

        }
    



       

