# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Home(View):
    TEMPALTES = 'home.html'

    def get(self, request):
        return render(request, self.TEMPALTES,{'active_menu':'home', })
