from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Despesa
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import DespesaSerializer

class DespesaListView(APIView):
    def get(self, request):
        despesas = Despesa.objects.all()
        serializer = DespesaSerializer(despesas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DespesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DespesaDetailView(APIView):
    def get(self, request, pk):
        despesa = get_object_or_404(Despesa, pk=pk)
        serializer = DespesaSerializer(despesa)
        return Response(serializer.data)
    
    def put(self, request, pk):
        despesa = get_object_or_404(Despesa, pk=pk)
        serializer = DespesaSerializer(despesa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        despesa = get_object_or_404(Despesa, pk=pk)
        despesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)