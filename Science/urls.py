from django.urls import path
from . import views
from .views import Science

urlpatterns = [
    path('Science', Science.as_view(),name='science'),
]
