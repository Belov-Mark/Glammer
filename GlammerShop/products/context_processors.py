from .models import Categories, Subcategory
from citys.models import City
from carts.models import Cart

def globalInfo(request):
    categories = Categories.objects.all()
    subcategories = Subcategory.objects.all()
    citys = City.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            item_count = cart.items.count()
        else:
            item_count = 0
    else:
        item_count = 0
    
    return {
        "categories": categories,
        "subcategories": subcategories,
        "citys": citys,
        "item_count": item_count,
    }