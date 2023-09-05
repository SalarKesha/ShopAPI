from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from account.models import Address, CustomUser
from account.serializers import AddressListSerializer, CustomUserListSerializer, CustomUserCreateSerializer
from lib.pagination import StandardPagination
from lib.permissions import HasAccountPermission


class AddressListCreateAPI(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer

    def get_queryset(self):
        qs = self.queryset.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CustomUserListAPI(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminUser]


class CustomUserCreateAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer


class CustomUserRetrieveUpdateAPI(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [IsAuthenticated, HasAccountPermission]


