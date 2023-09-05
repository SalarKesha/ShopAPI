import os.path

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import CustomUser, Address


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('title', 'points')


class CustomUserListSerializer(serializers.ModelSerializer):
    addresses = AddressListSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'image', 'addresses', 'password')


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'image')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_image(self, attr):
        if not attr:
            return attr
        file_extension = str(attr).split('.')[-1]
        if file_extension not in ['png', 'jpg', 'jpg']:
            raise ValidationError("file extension can be jpg, jpeg or png")
        file_size = attr.size
        if file_size > 200000:
            raise ValidationError("size of image must be less than 200kb")
        else:
            return attr

    def validate_password(self, attr):
        if len(attr) < 8:
            raise ValidationError("password must be more than 8 characters")
        return attr

    def create(self, validated_data):
        user = CustomUser(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if validated_data.get('password', False):
            user = CustomUser.objects.get(id=instance.id)
            user.set_password(validated_data['password'])
            user.save()
        return instance
