from rest_framework.permissions import BasePermission

from account.models import CustomUser


class HasAccountPermission(BasePermission):
    def has_permission(self, request, view):
        user = CustomUser.objects.filter(id=view.kwargs['pk']).first()
        if user:
            return request.user == user
        else:
            return False
