from django.urls import path
from . import views

urlpatterns = [
    path('News/', views.news)
]
