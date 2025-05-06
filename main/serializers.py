from rest_framework import serializers
from .models import Despesa

class DespesaSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)
    
    class Meta:
        model = Despesa
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')