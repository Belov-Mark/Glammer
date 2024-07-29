from .models import Slider
from products.models import Product
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/main.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newProducts'] = Product.objects.all().order_by('-created_at')[:6]
        context['saleProducts'] = Product.objects.filter(discount__gt=0).order_by('-created_at')[:3]
        context['slider1_slides'] = Slider.objects.filter(order__lte=9)
        context['slider2_slides'] = Slider.objects.filter(order__gt=10)
        return context

class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

