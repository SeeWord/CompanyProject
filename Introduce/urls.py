from django.urls import path
from . import views
from .views import Introduce

urlpatterns = [
    path('Introduce', Introduce.as_view(), name='methods'),
]
