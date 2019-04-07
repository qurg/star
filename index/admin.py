from django.contrib import admin
from .models import *

admin.site.site_title = '后台管理'
admin.site.site_header = '后台管理'


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight', 'size', 'type']

    search_fields = ['id', 'name', 'type__name']

    list_filter = ['name', 'type__name']

    ordering = ['id']

    # date_hierarchy = Field

    # 添加新数据的时候，允许输入的字段
    fields = ['name', 'weight', 'size', 'type']

    # 设置只读的字段
    # readonly_fields = ['name']

    # 显示
    list_display.append('colored_type')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['name']
        return self.readonly_fields
