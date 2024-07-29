from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Product

class CatalogView(ListView):
    # модель для работы представления
    model = Product

    # шаблон представления
    template_name = 'products/catalog.html'

    # имя переменной контекста
    context_object_name = 'products'

    # постраничная разбивка
    paginate_by = 1
    
    # показывать пустую страницу вместо ошибки 404
    allow_empty = False

    # имя параметра в url, по которому будет осуществляться постраничная разбивка
    slug_url_kwarg = 'category_slug'

    def get_queryset(self):
        # получает QuerySet с товарами
        category_slug = self.kwargs.get(self.slug_url_kwarg)

        if category_slug == 'all':
            # если slug категории 'all', то возвращает QuerySet со всеми товарами
            products = super().get_queryset()
        else:
            # если slug категории не 'all', то фильтрует товары по slug категории
            products = super().get_queryset().filter(category__slug=category_slug)
            if not products.exists():
                # если не нашлось товаров с указанным slug категории,
                # то выбрасывает исключение Http404
                raise Http404()
        return products


    def get_context_data(self, **kwargs):
        # получает контекст от родительского класса
        context = super().get_context_data(**kwargs)
        # добавляет slug категории в контекст
        context['slug_url'] = self.kwargs.get('category_slug')
        return context


class ProductView(DetailView):
    # модель, которую представляет данное представление
    model = Product
    # шаблон, используемый для отображения данных модели
    template_name = 'products/product.html'
    # имя параметра в url, по которому будет осуществляться получение объекта модели
    pk_url_kwarg = 'id'
    # имя контекстного объекта, представляющего объект модели
    context_object_name = 'product'

    # получает объект модели по значению pk_url_kwarg из url
    def get_object(self, queryset=None):
        # получает объект модели с указанным id или выбрасывает исключение Http404, если объекта нет
        product = get_object_or_404(Product, id=self.kwargs.get(self.pk_url_kwarg))
        return product
    
    # добавляет к контексту данные, необходимые для отображения
    def get_context_data(self, **kwargs):
        # получает контекст от родительского класса
        context = super().get_context_data(**kwargs)
        # добавляет название товара в контекст, чтобы его можно было использовать в шаблоне
        context['title'] = self.object.name
        return context


# Представление для отображения свежих товаров
class NewsView(ListView):
    # модель, которую представляет данное представление
    model = Product
    # шаблон, используемый для отображения данных модели
    template_name = 'products/news.html'
    # имя контекстного объекта, представляющего список свежих товаров
    context_object_name = 'newProducts'
    # количество товаров на странице
    paginate_by = 12
    # разрешает отображение пустой страницы
    allow_empty = False

    # получает QuerySet с свежими товарами
    def get_queryset(self):
        return Product.get_recent_products()

    # добавляет к контексту список свежих товаров
    def get_context_data(self, **kwargs):
        # получает контекст от родительского класса
        context = super().get_context_data(**kwargs)
        # добавляет список свежих товаров в контекст
        context['newProducts'] = self.get_queryset()
        return context

# Представление для отображения скидочных товаров
class SaleView(ListView):
    # модель, которую представляет данное представление
    model = Product
    # шаблон, используемый для отображения данных модели
    template_name = 'products/sale.html'
    # имя контекстного объекта, представляющего список скидочных товаров
    context_object_name = 'saleProducts'
    # количество товаров на странице
    paginate_by = 12
    # разрешает отображение пустой страницы
    allow_empty = False

    # получает QuerySet с скидочными товарами
    def get_queryset(self):
        return Product.objects.filter(discount__gt=0)

    # добавляет к контексту список скидочных товаров
    def get_context_data(self, **kwargs):
        # получает контекст от родительского класса
        context = super().get_context_data(**kwargs)
        # добавляет список скидочных товаров в контекст
        context['saleProducts'] = self.get_queryset()
        return context
