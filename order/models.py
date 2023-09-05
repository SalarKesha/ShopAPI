from django.db import models
from basket.models import Basket
from lib.models import BaseModel


class Order(BaseModel):
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT, related_name='orders')

    def __str__(self):
        return str(self.basket)
