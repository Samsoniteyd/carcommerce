from django.shortcuts import render

from rents.forms import RentForm

from datetime import datetime as dt

from . models import *
# Create your views here.


def rent(request):

    rent = Brand.objects.all()
    context = {
        'rent': rent
    }



    return render(request, 'rents/rent.html', context)

def fri(request, id):
     rent = Brand.objects.get(id=id)


     form = RentForm()

     if request.method == 'POST':
           forms = RentForm(request.POST or None)
           if forms.is_valid():
                Firstname = forms.cleaned_data.get('Firstname')
                Secondname = forms.cleaned_data.get('Secondname')
                mobile =forms.cleaned_data.get('mobile')
                address =forms.cleaned_data.get('address')
                date_of_booking= forms.cleaned_data.get('date_of_booking')
                date_of_return= forms.cleaned_data.get('date_of_return')
                total_days= date_of_booking-date_of_return
                total_amount= Brand.amount*total_days 
                Payment_method = forms.cleaned_data.get('Payment_method')

                rent= RentForm(Firstname=Firstname, Secondname=Secondname, mobile=mobile, address=address, date_of_booking=date_of_booking, date_of_return=date_of_return, total_days=total_days, total_amount=total_amount, payment_method=Payment_method)
                rent.save()

                # form.amount = (dt.strptime(form.end_date, "%Y/%m/%d") - dt.strptime(form.start_date, "%Y/%m/%d")).days
                # print('form.amount')
                # form = form.save(commit=False)
                
                
    

     context ={
         'rents': rent,
         'form': form
      }
     
     return render(request, 'rents/form.html', context )


def reg(request, id):
     rent= Brand.objects.get(id=id)
     context={
          'rents':rent
     }
     return render(request, 'rents/register.html', context)