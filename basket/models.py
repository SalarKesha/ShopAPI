from django.conf import settings
from django.db import models
from lib.models import BaseModel
from product.models import Product


class Basket(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='baskets')

    def __str__(self):
        return str(self.user)


class BasketLine(BaseModel):
    basket = models.ForeignKey(Basket, related_name='lines', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.basket)
