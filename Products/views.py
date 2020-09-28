# coding:utf-8
from django.shortcuts import render
from django.views import View
from .models import Product


class ProductBase(View):
    TEMPALTES = 'Product.html'

    def get(self, request):
        return render(request, self.TEMPALTES, {'active_menu': 'Product', })


class ProductList(View):
    TEMPALTES = 'Product.html'

    def post(self, request, productName):
        submenu = ''
        if self.request.method == 'POST':
            if productName == 'robot':
                productName = '智能家用机器人'
            elif productName == 'monitor':
                productName = '智能监控'
            elif productName == 'faceMg':
                productName = '人脸识别'
            else:
                productName = 'blank'
        productList = Product.objects.filter(producttype=productName).order_by('-publishdate')

        return render(request, self.TEMPALTES,
                      {'active_menu': 'products',
                       'sub_menu': submenu,
                       'productName': productName, 'productList': productList, })

    def Product(self, request, product_id):
        a = {'robot': '智能家用机器人', 'monitor': '智能监控', 'faceMg': '人脸识别', }
        submenu = product_id
        for key, values in a.items():
            if product_id == key:
                product_name = values
            else:
                product_name = 'blank'
        productList = Product.objects.filter(producttype=product_name).order_by('-publishdate')
        return render(request, self.TEMPALTES,
                      {'active_menu': 'products',
                       'sub_menu': submenu, 'productName': product_name, 'productList': productList, })
