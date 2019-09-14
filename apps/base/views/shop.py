# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

# Librerias de terceros
from apps.base.models import PyProduct

# Tienda de Productos

PRODUCT_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Descripción', 'field': 'description'},
    {'string': 'Precio', 'field': 'price'},
    {'string': 'Activo', 'field': 'web_active'},
    {'string': 'Código', 'field': 'code'},
    {'string': 'Código Barra', 'field': 'code'},
]


class WebProductView(ListView):
    """ Despleiga todos los poductos de la tienda con la posibilidad de
    filtralos por categoria
    """
    model = PyProduct
    template_name = 'shop/shop.html'
    fields = PRODUCT_FIELDS
    paginate_by = 8
    extend_from = None
    url_web_product = None
    queryset = PyProduct.objects.filter(web_active='True')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extend_from'] = self.extend_from
        context['url_web_product'] = self.url_web_product

        return context


class WebProductDetailView(DetailView):
    """Detalle del producto
    """
    model = PyProduct
    template_name = 'shop/product.html'
    extend_from = None
    url_web_shop = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extend_from'] = self.extend_from
        context['url_web_shop'] = self.url_web_shop

        return context