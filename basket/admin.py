from django.contrib import admin
from django.contrib.admin import register

from basket.models import Basket, BasketLine


class BasketLineInline(admin.TabularInline):
    model = BasketLine
    extra = 1


@register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user']
    inlines = [BasketLineInline]
