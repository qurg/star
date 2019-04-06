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


def model_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            weight = product.cleaned_data['weight']

            # 直接保存数据
            product.save()

            # 保存前有一些属性需要调整
            # product_db = product.save(commit=False)
            # product_db.name = 'change name'
            # product_db.save()

            # 保存多对多的表结构
            # product.save_m2m()

            return HttpResponse('提交成功，weight数据清洗后为：' + weight)
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())
