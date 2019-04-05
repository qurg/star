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
