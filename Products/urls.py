from django.urls import path
from . import views
from .views import ProductList

urlpatterns = [
    path('ProView', ProductList.as_view(), name='ProductView'),
]
#/<str:product_id>

