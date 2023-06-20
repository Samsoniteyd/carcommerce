
from django.shortcuts import render

# Create your views here.


from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect


from django.conf import settings

from django.contrib import messages

from django.core.mail import send_mail

from datetime import datetime as dt

from . forms import RegForm
# from django.views.generic import ListView

from . models import *
# Create your views here.




def home(request):
     cat= Rentage.objects.all()
     carousel= Slide.objects.all()
     context ={
          'cat': cat,
          "cara": carousel
     }
     return render(request, 'carrents/home.html', context)


def rent(request, id):

    rent = Brand.objects.all().filter(category_id=id)
    category = Rentage.objects.get(id=id)
    

    context = {
        'rent': rent,
        'cat': category,
       
    }



    return render(request, 'carrents/rent.html', context)




def fri(request, id):
    #  rent_id = request.session.get('rent_id', None)
    #  rent= Brand.objects.get(id=rent_id)
     rent= Brand.objects.get(id=id)
     if request.user.is_authenticated and request.user.profile:
       rent.customer = request.user.profile
       rent.save()
    #  else:
    #    return redirect('/user/login/?next=/payments/')

    #  else:
    #   return redirect('/users/login/?next=/form/')

     form= RegForm()
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
             paymethod = form.cleaned_data.get ('payment_method')
             

             form = Order( brand_id=rent.id, surname=sname, firstname=fname, middlename=mname, address=addr, email=email, phone=phn, date_of_birth=dob, booking=book, returnbooking=rbook,payment_method=paymethod )
             form.save()

             order = form.id
             if paymethod == "Paystack":
                return redirect('payments', id=order)
             send_mail(
             subject= 'registered',
             message= f'{sname} hgshdgehjsduhsjklajhlahdfuifjkahuhfnjfhurdjnndjhsjk',
             from_email= settings.EMAIL_HOST_USER,
             recipient_list = [email],
             fail_silently=False)
         return redirect('payments', id=order) 
            
               
               
     context ={
         
         'form': form,
         'rents':rent,
        
       }
    #  messages.warning(request, "login to book")
     
     return render(request, 'carrents/form.html', context)
    
    
    



def reg(request, id):
     rent= Brand.objects.get(id=id)
     context={
          'rents':rent
     }
     return render(request, 'carrents/register.html', context)

def payments(request, id):
    
    orders = Order.objects.get(id=id)
    # messages.success(request, 'rent successful')
    context ={
        'item': orders,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
    }
    return render(request, 'carrents/payments.html', context)

def verify_payment(request:HttpRequest, ref:str)-> HttpResponse:
    payment = get_object_or_404(Order, ref=ref)
    verified = payment.verify_payment()

    if verified:
        messages.success(request, 'verification successful')
    else:
        messages.warning(request, 'verification failed')
    return redirect('dashboard')    


def booking_list(request):
    return

























