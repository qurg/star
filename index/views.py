from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from index.form import *


# def index(request):
#     type_list = Product.objects.values('type').distinct()
#     name_list = Product.objects.values('name', 'type')
#     return render(request, 'index.html', locals())


def index(request):
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            name = product['name']
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())


class ProductList(ListView):
    context_object_name = 'type_list'

    template_name = 'index.html'

    queryset = Product.objects.values('type').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context
