from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from account.models import CustomUser, Address


@register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'image', 'created_time', 'modified_time']
    search_fields = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password', 'image')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'image'),
        }),
    )


@register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'points']
    search_fields = ['user']
