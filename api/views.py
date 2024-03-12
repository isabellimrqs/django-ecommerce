from django.shortcuts import render
from .models import Cliente
from .serializer import ClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def listar_clientes(request):
    if request.method == 'GET':
        queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
    return Response(serializer.data)