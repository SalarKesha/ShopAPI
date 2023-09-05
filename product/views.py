from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from lib.pagination import StandardPagination
from product.models import Category, Product
from product.serializers import ProductListSerializer, CategoryListSerializer, CategoryDetailSerializer, \
    ProductDetailSerializer


def test(request):
    return HttpResponse('product Page ...')


class CategoryListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = StandardPagination
    filterset_fields = ['title', 'category__title']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price', 'quantity']
    ordering = ['-quantity']

    def get_queryset(self):
        return self.queryset.filter(is_active=True)


class ProductDetailAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
