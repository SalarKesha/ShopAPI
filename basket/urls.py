from django.urls import path
from basket.views import BasketListAPI, BasketLineCreateAPI, BasketAPI, BasketLineUpdateAPI

urlpatterns = [
    path('', BasketAPI.as_view(), name='basket_detail'),
    path('list/', BasketListAPI.as_view(), name='basket_list'),
    path('line/create/', BasketLineCreateAPI.as_view(), name='basket_line_create'),
    path('line/update/<int:pk>/', BasketLineUpdateAPI.as_view(), name='basket_line_update'),
]
