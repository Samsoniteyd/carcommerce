from django.contrib import messages
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.core.mail import send_mail

from django.http import JsonResponse
import json

from .models import *

from django.core.paginator import Paginator

from django.db.models import Q

from . forms import CheckoutForm,ConForm
# Create your views here.


def index(request):
    sliders = Carousel.objects.all()
    category= Category.objects.all().order_by('-created_at')
    product= Product.objects.all().order_by('-created_at')[:6]
    offer= Product.objects.all().order_by('-created_at')[:2]
    vendor= Vendor.objects.all()
    #pagination
    # pagination = Paginator(category, 3)
    # page_number = request.GET.get('page')
    # page_list=pagination.get_page(page_number)
    context ={
        'sliders': sliders,
        'category': category,
        'product':product,
        'vendor': vendor,
        'offer': offer
        # 'paginator': page_list

    }
    return render(request, 'stores/index.html', context)


# category 
# category 

def category(request, id):
   product= Product.objects.all().filter(category_id=id)
   category= Category.objects.get(id=id)
   context={
        'product': product,
        'hd': category
    }
   return render(request, 'stores/category.html', context)


# product 
# product 
def product(request, id):
    products = Product.objects.get(id=id)
    context={
        'product': products     

    }
    return render(request, 'stores/product.html', context)


 # brands 
# brands 
def products(request):
        brand= Product.objects.all()
# pagination 
# pagination 

        pagination= Paginator(brand, 12)
        page_number = request.GET.get('page')
        page_list = pagination.get_page(page_number)

        context={
             'brands': brand,
             'paginator': page_list
        }
        return render(request, 'stores/products.html', context) 

def search(request):
     search= request.GET.get('search_word')
     product= Product.objects.filter(Q(title__icontains= search)|Q(description__icontains= search))
     context={
          'search': product
     }
     return render(request,'stores/search.html', context)


def more(request, id):
    product=Product.objects.get(id=id)
    context={
        'mor':product
    }
    return render(request, 'stores/more.html', context)     


#add to cart

def add_to_cart(request,id):
     #get particular product

     cart_product = Product.objects.get(id=id)
      #create a cart id base on session
     cart_id =request.session.get('cart_id', None)
     #check if cart exists
     if cart_id:
        #   getting the available cart 
        cart_item = get_object_or_404(Cart, id=cart_id)# Cart.objects.get(id=cart_id)

          #check authentication
        if request.user.is_authenticated and request.user.profile:
              cart_item.customer = request.user.profile
              cart_item.save()
     
        #  check if product exist in cart  
        this_product_in_cart = cart_item.cartitem_set.filter(product= cart_product) #child to parent relationship
        if this_product_in_cart.exists():
               cartproduct= this_product_in_cart.last()
               cartproduct.quantity +=1
               cartproduct.subtotal += cart_product.price
               cartproduct.save()
               cart_item.total += cart_product.price
               cart_item.save()
                #message item/product increased in cart successfully  
               

        else:
               cartproduct = CartItem.objects.create(cart=cart_item, product=cart_product, quantity= 1, subtotal=cart_product.price )

               cart_item.total += cart_product.price

               cart_item.save() 
               #message a new product has been created successfully  


     else:
        cart_item = Cart.objects.create(total=0)
        request.session['cart_id'] = cart_item.id

        cartproduct = CartItem.objects.create(cart=cart_item, product=cart_product, quantity= 1, subtotal=cart_product.price )

        cart_item.total += cart_product.price

        cart_item.save()
        #message anew cart created successfully
     return redirect('products')

def add_to_wish(request,id):
      #get particular product

     wish_product = Product.objects.get(id=id)
      #create a cart id base on session
     wish_id =request.session.get('wish_id', None)
     

     wish_item= WishlistItem.objects.get(id=wish_id)

        #   check for authentication 
     if request.user.is_authenticated and request.user.profile:
              wish_item.customer = request.user.profile
              wish_item.save()

     else:
          wish_item= WishlistItem.objects.create(total=0)
          request.session['wish_id']= wish_item.id
          wishproduct = CartItem.objects.create(cart=wish_item, product=wish_product, quantity=1, subtotal=wish_product)
          wish_item.total += wishproduct
          wish_item.save()

          return redirect('products') 
 


def wish(request):
     #session
    wish_id = request.session.get('wish_id', None)

    if wish_id:
          # getting the available cart
        wish_item = get_object_or_404(WishlistItem, id=wish_id)#  Cart.objects.get(id=cart_id)
        #check authentication
        if request.user.is_authenticated and request.user.profile:
              wish_item.customer = request.user.profile
              wish_item.save()
    else:
          wish_item= None     

    context = {
         'wishes': wish_item  
    }      
          
    return render(request, 'stores/wish.html', context)

def mycart(request):
     #session
    cart_id = request.session.get('cart_id', None)

    if cart_id:
          # getting the available cart
        cart_item = get_object_or_404(Cart, id=cart_id)#  Cart.objects.get(id=cart_id)
        #check authentication
        if request.user.is_authenticated and request.user.profile:
              cart_item.customer = request.user.profile
              cart_item.save()
    else:
          cart_item= None     

    context = {
         'cart': cart_item  
    }      
          
    return render(request, 'stores/mycart.html', context)



def managecart(request, id):
     action = request.GET.get('action')
     cart_obj = CartItem.objects.get(id=id)
     cart = cart_obj.cart

     if action == 'inc':
          cart_obj.quantity +=1
          cart_obj.subtotal += cart_obj.product.price
          cart_obj.save()
          cart.total += cart_obj.product.price
          cart.save()

     if action == 'dcr':
          cart_obj.quantity -=1
          cart_obj.subtotal -= cart_obj.product.price
          cart_obj.save()
          cart.total -= cart_obj.product.price
          cart.save() 

          if cart_obj.quantity == 0:
               cart_obj.delete()

     if action == 'del':
          cart.total -= cart_obj.subtotal
          cart.save()
          cart_obj.delete()              
     return redirect('mycart')


def checkout(request):
    cart_id = request.session.get('cart_id', None)
    cart_obj = Cart.objects.get(id=cart_id)

    form = CheckoutForm()
    #check authentication
    if request.user.is_authenticated and request.user.profile:
        pass
    else:
        return redirect('/users/login/?next=/checkout/')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST or None)
        if form.is_valid():                                               
            form = form.save(commit=False)
            form.cart = cart_obj
            form.amount = cart_obj.total
            form.subtotal = cart_obj.total 
            form.discount = 0
            paymethod = form.payment_method
            del request.session['cart_id']
            form.save()  

            order = form.id
            if paymethod == 'Paystack':
                return redirect('payment', id=order)
            
            # elif paymethod == 'Trnasfer':
            #     return redirect('trpayment', id=order)
                
                 

    context= {
        'form':form,
        'cart':cart_obj

    }

    return render(request, 'stores/checkout.html',context)


def payment(request, id):
    orders = Order.objects.get(id=id)
 
    context ={
        'order': orders,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
    }
    return render(request, 'stores/payment.html', context)

def verify_payments(request:HttpRequest, ref:str)-> HttpResponse:
    payment = get_object_or_404(Order, ref=ref)
    verified = payment.verify_payments()

    if verified:
        messages.success(request, 'verification successful')
    else:
        messages.warning(request, 'verification failed')
    return redirect('dashboard')    


def contact(request):
     form = ConForm()
     if request.method == "POST":          
         form= ConForm(request.POST)
         if form.is_valid():
             First_Name = form.cleaned_data.get('First_Name')
             Last_Name = form.cleaned_data.get('Last_Name')
             Mobile = form.cleaned_data.get('Mobile')
             Email = form.cleaned_data.get ('Email')
             Subject = form.cleaned_data.get('Subject')
             Message =form.cleaned_data.get('Message')
             created = form.cleaned_data.get ('created')
            
             

             form = Contacts( First_Name=First_Name, Last_Name=Last_Name, Mobile=Mobile, Email=Email, Subject=Subject, Message=Message, created=created)
             form.save()

            
             
            #  send_mail(
            #  subject= 'registered',
            #  message= f'{First_Name} we are happy to provide good services',
            #  from_email= settings.EMAIL_HOST_USER,
            #  recipient_list = [Email],
            #  fail_silently=False)
             messages.success(request, 'message sent successful')
         return redirect('index') 


     context= {
          'form':form
     }
     return render(request, 'stores/contact.html', context)

def about (request):
     return render(request, "stores/about.html",)


# def updateItem(request):
#      data = json.loads(request.data)
#      productId = data['productId']
#      action = data['action']

#      print('Action:', action)
#      print('productId:', productId)

#      customer = request.user.customer
#      product = product.objects.get(id=productId)
#      cart_obj = Cart.objects.get(id=cart_id)
#      return JsonResponse('item was added', safe=False)