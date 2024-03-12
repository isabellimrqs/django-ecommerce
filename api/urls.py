from django.urls import path
from . import views

urlpatterns = [
    path('clientes', views.listar_clientes)
]