# coding:utf-8
from django.http import HttpResponse


def service (request):
    html = '<html> <body> 提供服务 </body> </html>'
    return HttpResponse(html)
