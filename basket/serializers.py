from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from basket.models import BasketLine, Basket
from product.models import Product
from product.serializers import ProductListSerializer


class BasketLineSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = BasketLine
        fields = ('id', 'product', 'quantity')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class BasketLineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketLine
        fields = ('product', 'quantity')

    def validate(self, attrs):
        product = Product.objects.filter(pk=(attrs['product']).pk).first()
        if product:
            if product.quantity < attrs['quantity']:
                raise ValidationError('quantity is more than number of product')
            return attrs
        raise ValidationError('product-id is not valid')


class BasketSerializer(serializers.ModelSerializer):
    lines = BasketLineSerializer(many=True)
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Basket
        fields = ('id', 'user', 'lines')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class BasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('user',)
        extra_kwargs = {
            'user': {'read_only': True}
        }
