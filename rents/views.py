from django.shortcuts import render

from rents.forms import RentForm

from django.contrib import messages

from datetime import datetime as dt

from . models import *
# Create your views here.




def home(request):
     cat= Rentage.objects.all()
     context ={
          'cat': cat
     }
     return render(request, 'rents/home.html', context)


def rent(request, id):

    rent = Brand.objects.all().filter(category_id=id)
    category = Rentage.objects.get(id=id)
    context = {
        'rent': rent,
        'cat': category
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
                total_days= forms.cleaned_data.get('total_days')
                total_amount= Brand.amount*total_days 
                Payment_method = forms.cleaned_data.get('Payment_method')

               #  total_days= date_of_return-date_of_booking

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