from .models import Categories, Subcategory
from citys.models import City

def globalInfo(request):
    categories = Categories.objects.all()
    subcategories = Subcategory.objects.all()
    citys = City.objects.all()
    
    return {
        "categories": categories,
        "subcategories": subcategories,
        "citys": citys,
    }