from . models import Category,Cartitem


def categorys(request):
    cats = Category.objects.filter()

    return{
        'catloops': cats
    }


def allcarts(request):
    
    if request.session.get('cart_id', None):
        cart= Cartitem.objects.filter()
        total = cart.count()
    elif request.user:
        cart= Cartitem.objects.filter()
        total = cart.count()
        
        return{
            'carts':total
        }
    