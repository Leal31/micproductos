from django.urls import path, include
from . import views
urlpatterns = [
    path('ProductoCrud', views.ProductoCrud)

]
