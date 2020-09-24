from django.urls import path
from . import views
from .views import IntroView

urlpatterns = [
    path('IntroView', IntroView.as_view(), name='IntroduceView'),
]
