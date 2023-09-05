from django.core.validators import FileExtensionValidator
from django.db import models
from lib.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Product(BaseModel):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(default=0)
    quantity = models.SmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                             upload_to='products/', blank=True, null=True)

    def __str__(self):
        return str(self.product)


class ProductAttribute(BaseModel):
    title = models.CharField(max_length=42)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.title

