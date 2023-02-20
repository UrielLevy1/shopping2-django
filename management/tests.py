from django.core.management.base import BaseCommand, CommandError
from product.models import Product

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    
    def test_func():
        print(Product.name)