from django.db import models
from product.models import Product

# Create your models here.


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    
    def __str__(self):
        return self.product.name
