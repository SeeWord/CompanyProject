# coding:utf-8
from django.http import HttpResponse


def products (request):
    html = '<html> <body> 公司产品列表 </body> </html>'
    return HttpResponse(html)