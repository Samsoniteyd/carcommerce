from django.shortcuts import render

# Create your views here.


from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect


from django.conf import settings

from django.contrib import messages

from . forms import RegForm

from datetime import datetime as dt

from . models import *
# Create your views here.




def home(request):
     cat= Rentage.objects.all()
     context ={
          'cat': cat
     }
     return render(request, 'carrents/home.html', context)


def rent(request, id):

    rent = Brand.objects.all().filter(category_id=id)
    category = Rentage.objects.get(id=id)
    context = {
        'rent': rent,
        'cat': category
    }



    return render(request, 'carrents/rent.html', context)




def fri(request, id): 
     rent= Brand.objects.get(id=id)
     
     if request.method == "POST":          
         form= RegForm(request.POST)
         if form.is_valid():
             sname = form.cleaned_data.get('surname')
             fname = form.cleaned_data.get('firstname')
             mname = form.cleaned_data.get('middlename')
             dob = form.cleaned_data.get ('date_of_birth')
             phn = form.cleaned_data.get('phone')
             email =form.cleaned_data.get('email')
             addr = form.cleaned_data.get ('address')
             book = form.cleaned_data.get ('booking')
             rbook = form.cleaned_data.get ('returnbooking')
             rental= Order( surname=sname, firstname=fname, middlename=mname, address=addr, email=email, phone=phn, date_of_birth=dob, booking=book, returnbooking=rbook )
             forms = form.save(commit=False)
             forms.rental= rental
             forms.save()  
             return redirect('form')
     else:
         form= RegForm()           
               
     context ={
         
         'form': form,
         'rents':rent

       }
     
     return render(request, 'carrents/form.html', context )


def reg(request, id):
     rent= Brand.objects.get(id=id)
     context={
          'rents':rent
     }
     return render(request, 'carrents/register.html', context)

def payment(request):
    orders = Order.objects.all()
    # days = orders.getnumdays
    # amount = orders.gettotalamount
    
    context ={
        'order': orders,
        # 'days': days,
        # 'amount': amount,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
    }
    return render(request, 'carrents/payment.html', context)

def verify_payment(request:HttpRequest, ref:str)-> HttpResponse:
    payment = get_object_or_404(Order, ref=ref)
    verified = payment.verify_payment()

    if verified:
        messages.success(request, 'verification successful')
    else:
        messages.warning(request, 'verification failed')
    return redirect('rent')    












#   #  back = request.POST['brand']
#         #  sname = request.POST['surname']
#         #  fname = request.POST['firstname']
#         #  mname = request.POST['middlename']
#         #  dob = request.POST['date_of_birth']
#         #  phn = request.POST['phone']
#         #  email = request.POST['email']
#         #  addr = request.POST['text']
#         #  book = request.POST['booking']
#         #  rbook = request.POST['returnbooking']

#         #  if dob >= date(2003-9-1):
#         #      messages.warning(request,'you are not allowed to rent a car')
#         #      return redirect('form')

#         #  info = Order(brand=back,surname=sname,firstname=fname,middlename=mname,text=addr,email=email,phone=phn,date_of_birth=dob,booking=book,returnbooking=rbook)
#         #  info.save()
#         #  return redirect('payment')



















