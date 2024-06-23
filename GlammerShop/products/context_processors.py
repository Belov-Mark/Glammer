from .models import Categories, Subcategory

def globalCategoriesAndSubcategories(request):
    categories = Categories.objects.all()
    subcategories = Subcategory.objects.all()
    return {
        "categories": categories,
        "subcategories": subcategories,
    }