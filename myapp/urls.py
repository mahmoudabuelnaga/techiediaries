from django.urls import path
from .views import (
    ProductListAPI,
    ProductDetailAPI,
    FamilyListAPI,
    FamilyDetailApi,
    LocationListAPI,
    LocatinDetailAPI,
    TransectionListAPI,
    TransectionDetailAPI
)

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name='product_list_api'),
    path('products/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail_api'),
    path('family/', FamilyListAPI.as_view(), name='family_list_api'),
    path('family/<int:pk>/', FamilyDetailApi.as_view(), name='family_detail_api'),
    path('location/', LocationListAPI.as_view(), name='location_list_api'),
    path('location/<int:pk>/', LocatinDetailAPI.as_view(), name='location_detail_api'),
    path('transection/', TransectionListAPI.as_view(), name='transection_list_api'),
    path('transection/<int:pk>/', TransectionDetailAPI.as_view(), name='transection_detail_api'),
]

