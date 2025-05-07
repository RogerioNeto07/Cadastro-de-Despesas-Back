from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, mixins
from .models import Despesa
from .serializers import DespesaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer