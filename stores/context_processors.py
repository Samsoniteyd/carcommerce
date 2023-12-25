from . models import *

def categorys(request):
    cats = Category.objects.filter()

    return{
        'catloops': cats
    }


def allcart(request):
    
    if request.session.get('cart_id', None):
        cart= CartItem.objects.filter()

    #    cart= Cart.objects.get(id=cart_id)
        total = cart.count()
    elif request.user:
       cart= CartItem.objects.filter()
        # cart= Cart.objects.get(id=cart_id)
       total = cart.count()
        
    return{
            'carts':total
        }
    
# def wish(request):
#     if request.session.get('wish_id', None):
#         listwish=WishlistItem.objects.filter()

#         total= listwish.count()
#     elif request.user:
#         listwish=WishlistItem.objects.filter()

#         total= listwish.count()

#     return{
#         "like":total
#     }

