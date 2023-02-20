from django.db import models
from product.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    
    def __str__(self):
        return self.product.name
