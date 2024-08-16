from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .products import products

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        '/api/products',
        '/api/products/create',
        '/api/products/upload',
        '/api/products<id>/reviews',
        '/api/products/top',
        '/api/products/<id>',
        '/api/products/delete/<id>',
        '/api/products/<update>/<id>',
    ]
    return Response(routes) # type: ignore

@api_view(['GET'])
def getProducts(request):
    return Response(products) # type: ignore


@api_view(['GET'])
def getProduct(request,pk):
    
    product = None
    
    for pro in products:
        if pro['_id'] == pk:
            product = pro
    return Response(product) # type: ignore
