from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import *
from .serializer import *

# Create your views here.
@api_view(['GET', 'POST'])
def ProductoCrud(request):

    if request.method == 'GET': # user requesting data
        query = Productos.objects.all()
        serializer = ProductoSerializers(query, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # user posting data
        serializer = ProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ProductoCrudOne(request, pk):
    try:
        producto = Productos.objects.get(codigo_producto=pk)
    except Productos.DoesNotExist:
        return JsonResponse({'message': 'El producto no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        producto_serializer = ProductoSerializers(producto)
        return Response(producto_serializer.data)

    elif request.method == 'PUT':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializers(producto,data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse(producto_serializer.data)
        return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return JsonResponse({'message' : 'El producto fue satisfactoriamente eliminado'}, status=status.HTTP_204_NO_CONTENT)
