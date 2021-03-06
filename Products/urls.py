from django.urls import path
from .views import ProductList, ProductBase

urlpatterns = [
    path('ProView', ProductBase.as_view(), name='ProductView'),
    path('ProView/Robot', ProductList.as_view(), name='robot'),
    path('ProView/Monitor', ProductList.as_view(), name='monitor'),
    path('ProView/FaceMg', ProductList.as_view(), name='faceMg'),
]
# /<str:product_id>
