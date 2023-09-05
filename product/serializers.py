from rest_framework import serializers
from rest_framework.serializers import ListSerializer

from product.models import Category, Product, ProductAttribute


class ProductAttribureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ('title', 'value')


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'products')

    def get_products(self, obj):
        return obj.products.count()


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ProductDetailSerializer(serializers.ModelSerializer):
    attributes = ProductAttribureSerializer(many=True)
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = ('title', 'category', 'price', 'discount', 'quantity', 'description', 'attributes', 'is_active')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'discount', 'quantity')
        extra_kwargs = {
            'id': {'read_only': True}
        }
