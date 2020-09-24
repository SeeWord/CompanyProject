# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IntroView(View):
    TEMPALTES = 'Introduce.html'

    def survey(self, request):
        return render(request, self.TEMPALTES, {'active_menu': 'Introduce', 'sub_menu': 'survey'})

    def honor(self, request):
        return render(request, self.TEMPALTES, {'active_menu': 'Introduce', 'sub_menu': 'honor'})
