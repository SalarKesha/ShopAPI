from django.contrib import admin
from django.contrib.admin import register

from product.models import ProductImage, ProductAttribute, Product, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@register(Product)
class ProductAmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'discount', 'quantity', 'category', 'is_active']
    list_filter = ['is_active']
    inlines = [ProductImageInline, ProductAttributeInline]
