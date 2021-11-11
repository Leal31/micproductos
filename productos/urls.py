from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename= 'productos')

urlpatterns = [
    path('', include(router.urls)),
]
