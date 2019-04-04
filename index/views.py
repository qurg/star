from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from index.models import Product


def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    return render(request, 'index.html', locals())


class ProductList(ListView):
    context_object_name = 'type_list'

    template_name = 'index.html'

    queryset = Product.objects.values('type').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context
