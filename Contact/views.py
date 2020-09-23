# coding:utf-8
from django.http import HttpResponse


def Contact (request):
    html = '<html> <body> 联系我们 </body> </html>'
    return HttpResponse(html)
