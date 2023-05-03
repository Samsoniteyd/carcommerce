from django.db import models

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
    amount = models.IntegerField(null=True)
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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=255)
    Secondname = models.CharField(max_length=255)
    address  = models.TextField()
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=50)
    total= models.CharField(max_length=255, null=True)
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS, default='pending')
    date_of_booking = models.DateField(blank=True, null=True)
    date_of_return = models.DateField(blank=True, null=True)
    total_days  = models.IntegerField(null=True)
    amount = models.IntegerField(blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    isAvailable = models.BooleanField(default=True)    
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD, default='paystack')
    ref = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return f'{self.order_status}::: {self.id}'

   