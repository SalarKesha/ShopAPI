from django.urls import path

from product.views import test, CategoryListAPI, ProductListAPI, ProductDetailAPI

urlpatterns = [
    path('', test, name='test'),
    path('category/list/', CategoryListAPI.as_view(), name='category_list'),
    path('list/', ProductListAPI.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailAPI.as_view(), name='product_detail'),
]
