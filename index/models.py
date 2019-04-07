from django.db import models

# Create your models here.
from django.utils.html import format_html


class Type(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('类型', max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    weight = models.CharField('重量', max_length=20)
    size = models.CharField('尺寸', max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='类型')

    def __str__(self):
        return self.name

    def colored_type(self):
        if '手机' in self.type.name:
            color_code = 'red'
        else:
            color_code = 'yellow'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            self.type,
        )
    colored_type.short_description = '带颜色的类型'

    # 用来定义Admin网站的中文显示
    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'
