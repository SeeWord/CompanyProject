from django.urls import path
from . import views
from .views import Productlist

urlpatterns = [
    path('ProView/<str:productName>', Productlist.as_view(), name='ProductView'),
]
