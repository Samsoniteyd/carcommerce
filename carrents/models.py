from django.db import models
import pandas as pd
import numpy as np
# Create your models here.
from django.db import models
from users.models import Profile
from datetime import date
import secrets

from . paystack import Paystack
# Create your models here.

class Rentage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='rentage', null=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


FUEL= (
    ('petrol', 'petrol'),
    ('diesel', 'diesel')
)

class Brand(models.Model):
    category =  models.ForeignKey(Rentage, on_delete=models.CASCADE)
   
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brand', null=True)
    description = models.TextField( max_length=255)
    discount = models.PositiveIntegerField( null=True, default=0, blank=True )
    amounts = models.IntegerField(null=True)
    inventory  = models.PositiveIntegerField()
    created_at  = models.DateField( auto_now_add= True)
    fuel = models.CharField(max_length=50, choices=FUEL, null=True)
    capacity = models.CharField(max_length=50, null=True)
    




    def __str__(self) ->str:
        return self.title  

   
ORDER_STATUS=(
    ('Pending', 'Pending'),
    ('Cancel Payment','Cancel Payment' ),
    ('Payment Received','Payment Received'),
    ('Order in progress', 'Order in progress'),
    ('Order Received','Order Received'),
)


PAYMENT_METHOD=(
    ('Paystack','Paystack'),
    ('Transfer', 'Transfer')
)
 





class Order(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='item')
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True )
    surname= models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255, null=True)
    middlename = models.CharField(max_length=255, null=True)
    address  = models.TextField()
    email= models.EmailField(max_length=255)
    phone = models.CharField(max_length=50)
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS, default='pending')
    date_of_birth = models.DateField(blank=True, null=True)
    booking = models.DateField(blank=True, null=True)
    returnbooking = models.DateField(blank=True, null=True)
    total_days  = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50, blank=True, null=True)
    isAvailable = models.BooleanField(default=True)    
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD, default='paystack')
    payment_complete = models.BooleanField(default=False)
    ref = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
     return f'{self.order_status}::: {self.id}'

    def save(self,*args, **kwargs):
        self.total_days = 0
        returnbooking = pd.to_datetime(self.returnbooking).date()
        booking = pd.to_datetime(self.booking).date()
        self.total_days = np.busday_count(booking,returnbooking)

        self.amount= 0
        amount = self.brand.amounts * int( self.total_days)
        self.amount = amount

        super(Order,self).save(*args, **kwargs)

    # def __str__(self) ->str:
    #     return f'{self.firstname}::: {self.id}:::{self.booking}::::{self.returnbooking}'

#  ref generate
    # def save(self, *args, **kwargs):
    #     while not self.ref:
    #         ref =secrets.token_urlsafe(50)
    #         obj_with_sm_ref = Order.objects.filter(ref=ref)
    #         if not obj_with_sm_ref:
    #             self.ref = ref
    #     super().save(*args, **kwargs)

    # #amount

    # def amount_value(self)-> int:
    #     return self.amount * 100     

    #verification

# def verify_payment(self):
#     paystack = Paystack()
#     status, result = paystack.verify_payment(self.ref, self.amount)
#     if status:
#             if result['total_amount'] / 100 == self.amount:
#                 self.payment_complete = True
#                 self.payment_method = 'Payment Received'
#             else:
#                 self.payment_method = 'Cancel Payment'


#             self.save()
#     if self.payment_complete:
#             return True
#     return False  


    