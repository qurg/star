from django import forms
from django.core.exceptions import ValidationError

from .models import *


def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='名字',
                           widget=forms.widgets.TextInput(attrs={'class': 'cl'}),
                           error_messages={'required': '名字不能为空'},
                           )
    weight = forms.CharField(max_length=50, label='重量',
                             validators=[weight_validate],
                             )
    size = forms.CharField(max_length=50, label='尺寸')

    # 设置下拉框
    choice_list = [(i + 1, v['name']) for i, v in enumerate(Type.objects.values('name'))]
    type = forms.ChoiceField(
        widget=forms.widgets.Select(attrs={'class': 'type', 'size': '4'}),
        choices=choice_list,
        label='产品类型',
    )


class ProductModelForm(forms.ModelForm):
    # 添加模型外的表单字段
    productId = forms.CharField(max_length=20, label='产品序号')

    class Meta:
        model = Product

        # 将所有字段转化
        # fields = '__all__'
        fields = ['name', 'weight', 'size', 'type']

        # 用于禁止模型字段转化为表单字段
        exclude = []

        # labels用于设置HTML元素控件的标签
        labels = {
            'name': '产品名称',
            'weight': '重量',
            'size': '尺寸',
            'type': '产品类型',
        }

        # 定义widgets,设置表单字段的CSS
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'c1'}),
        }

        # 定义字段类型
        field_classes = {
            'name': forms.CharField,
        }

        # 帮助提示信息
        help_texts = {
            'name': 'name help',
        }

        # 自定义报错信息
        error_messages = {
            # 设置全部的报错信息
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入的内容', },
            'weight': {'required': '请输入重量数据',
                       'invalid': '请检查数值是否正确', },
        }

    # 自定义数据字段清洗
    def clean_weight(self):
        data = self.cleaned_data['weight']
        return data + 'g'

    def __init__(self, *args, **kwargs):
        super(ProductModelForm, self).__init__(*args, **kwargs)

        type_obj = Type.objects.values('name')
        choice_list = [(i + 1, v['name']) for i, v in enumerate(type_obj)]
        self.fields['type'].choices = choice_list

