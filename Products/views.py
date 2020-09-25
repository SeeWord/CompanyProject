# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.handlers.wsgi import WSGIRequest

class ProductList(View):
    TEMPALTES = 'Product.html'

    def get(self, request):
        return render(request, self.TEMPALTES, {'active_menu': 'Product', })

    # def products(self,request,productName):
    #     submenu = productName
    #     if productName == 'robot':
    #         productName == '智能家用机器人'
    #     elif productName == 'monitor':
    #         productName == '智能监控'
    #     elif productName == 'faceMg':
    #         productName == '人脸识别'
    #     else:
    #         productName == 'blank'
    #     productList = ProductList.objects.fliter(productType=productName).order_by('-publishDate')
    #     return render(request, self.TEMPALTES,
    #                   {'active_menu': 'products',
    #                    'sub_menu': submenu,
    #                    'productName': productName, })

    def product(self, request, product_id):
        a = {'robot': '智能家用机器人', 'monitor': '智能监控', 'faceMg': '人脸识别', }
        submenu = product_id
        for i in a.items():
            if product_id == i.keys():
                product_name = i.values()
            else:
                product_name = 'blank'
        return render(request, self.TEMPALTES,
                      {'active_menu': 'products', 'sub_menu': submenu, 'productName': product_name, })
