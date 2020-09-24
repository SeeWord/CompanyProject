# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Productlist(View):
    TEMPALTES = 'Product.html'

    def get(self, request):
        return render(request, self.TEMPALTES, {'active_menu': 'Product', })

    def prolist(self, request, productName):
        a = {'robot': '智能家用机器人', 'monitor': '智能监控', 'faceMg': '人脸识别', }
