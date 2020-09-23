# coding:utf-8
from django.http import HttpResponse


def news (request):
    html = '<html> <body> 公司新闻 </body> </html>'
    return HttpResponse(html)
