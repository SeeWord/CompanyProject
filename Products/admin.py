# coding:utf-8

from django.contrib import admin

from .models import Product, ProductImg


class ProductImgInline(admin.StackedInline):#创建内联模型管理器
    model = ProductImg
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline, ]


admin.site.register(Product, ProductAdmin)
