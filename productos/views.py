from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all().order_by('codigo_producto')
    serializer_class = ProductoSerializers
