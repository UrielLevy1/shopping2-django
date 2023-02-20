from django.shortcuts import render

# Create your views here.


# /localhost:8000/products
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST', 'DELETE'])
def products(request):
    """
    List all cartitems, or create a new product
    """
    if request.method == 'GET': # list products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # create new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    elif request.method == 'DELETE': # delete product
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'DELETE', 'PUT'])
def product(request, pk):
    product = Product.objects.get(id=pk)   

    """
    Get a single product, update or delete one
    """
    
    if request.method == 'PUT': # update a product 
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET': # get product
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    
    elif request.method == 'DELETE': # delete product
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
# @api_view(['GET', 'PUT', 'POST'])
# def add_product_to_cart(request, pk):
#     product = Product.objects.get(id=pk)  
    
#     """
#     Add product to cart
#     """ 