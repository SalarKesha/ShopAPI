from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from lib.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    image = models.FileField(upload_to='users/',
                             validators=[FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'png'))], null=True,
                             blank=True)

    def __str__(self):
        return self.username


class Address(BaseModel):
    title = models.TextField(max_length=200)
    points = models.JSONField(default=dict, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='addresses', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        return str(self.user)
