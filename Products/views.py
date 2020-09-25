# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from Products.models import Product


class ProductList(View):
    TEMPALTES = 'Product.html'

    def get(self, request):
        return render(request, self.TEMPALTES, {'active_menu': 'Product', })

    def post(self, request, *args):
        submenu = ''
        productName = ''
        if self.request.method == 'POST':
            if args == 'robot':
                productName == '智能家用机器人'
            elif args == 'monitor':
                productName == '智能监控'
            elif args == 'faceMg':
                productName == '人脸识别'
            else:
                productName == 'blank'
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
        productList = ProductList.objects.fliter(productType=product_name).order_by('-publishDate')
        return render(request, self.TEMPALTES,
                      {'active_menu': 'products',
                       'sub_menu': submenu, 'productName': product_name, 'productList': productList, })
