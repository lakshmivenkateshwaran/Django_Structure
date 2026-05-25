from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer

# Get method
@api_view(['GET', 'POST'])
def products(request):

    # GET API
    if request.method == 'GET':

        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    # POST API
    elif request.method == 'POST':

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Category APIs   
@api_view(['GET'])
def categories(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

# Get single product
@api_view(['GET'])
def get_product(request, id):

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)

    return Response(serializer.data)