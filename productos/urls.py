from django.urls import path, include
from . import views
urlpatterns = [
    path(r'Productos', views.ProductoCrud),
    path(r'Productos/<int:pk>', views.ProductoCrudOne)

]
