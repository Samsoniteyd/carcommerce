from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(WishlistItem)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Contacts)
