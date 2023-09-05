from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from basket.models import Basket, BasketLine
from basket.serializers import BasketSerializer, BasketCreateSerializer, BasketLineSerializer, \
    BasketLineCreateSerializer


class BasketAPI(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        last_basket = self.queryset.filter(user=self.request.user).latest()
        return [last_basket, ]


class BasketListAPI(ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BasketCreateSerializer
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class BasketLineCreateAPI(CreateAPIView):
    queryset = BasketLine.objects.all()
    serializer_class = BasketLineCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        user = self.request.user
        last_basket = user.baskets.latest()
        serializer.save(basket=last_basket)


class BasketLineUpdateAPI(RetrieveUpdateDestroyAPIView):
    queryset = BasketLine.objects.all()
    serializer_class = BasketLineCreateSerializer
    permission_classes = [IsAuthenticated, ]
