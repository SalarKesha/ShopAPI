from django.contrib import admin
from django.contrib.admin import register

from order.models import Order


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['basket']
