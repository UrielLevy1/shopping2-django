from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer


@api_view(['GET', 'POST', 'DELETE'])
def cartitems(request):
    """
    List all cartitems, or create a new cartitem
    """
    if request.method == 'GET': # list products
        cartItems = CartItem.objects.all()
        serializer = CartItemSerializer(cartItems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # create new product
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': # delete product
        cartitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
@api_view(['GET', 'DELETE', 'PUT'])
def cartitem(request, pk):
    cartitem = CartItem.objects.get(id=pk)
    """
    Get a single cartitem, update or delete one
    """
    if request.method == 'PUT': # update cartitem
        serializer = CartItemSerializer(cartitem, data=request.data, status=status.HTTP_200_OK)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET': # get single cartitem
        serializer = CartItemSerializer(cartitem, many=False)
        return Response(serializer.data)
    
    elif request.method == 'DELETE': # delete cartitem
        cartitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
    
#     {
#     "name": "Xiomi 2 cover edited",
#     "description": "this is no such a great cover 2",
#     "price": "150"
# }