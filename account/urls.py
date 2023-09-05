from django.urls import path

from account.views import AddressListCreateAPI, CustomUserListAPI, CustomUserCreateAPI, CustomUserRetrieveUpdateAPI

urlpatterns = [
    path('address/list/', AddressListCreateAPI.as_view(), name='address_list'),
    path('address/create/', AddressListCreateAPI.as_view(), name='address_create'),
    path('user/list/', CustomUserListAPI.as_view(), name='user_list'),
    path('user/create/', CustomUserCreateAPI.as_view(), name='user_create'),
    path('user/update/<int:pk>/', CustomUserRetrieveUpdateAPI.as_view(), name='user_update'),
]
