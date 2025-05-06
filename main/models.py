from django.db import models
from django.core.validators import MinValueValidator

class Despesa(models.Model):
    CATEGORIAS = [
        ('LAZER', 'Lazer'),
        ('CONTAS', 'Contas'),
        ('MERCADO', 'Mercado'),
        ('SAUDE', 'Saúde'),
        ('COMIDA', 'Comida'),
        ('TRANSPORTE', 'Transporte'),
        ('EDUCACAO', 'Educação'),
        ('OUTROS', 'Outros'),
    ]

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='OUTROS'
    )
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data', '-created_at']  # Corrigido aqui
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return f"{self.get_categoria_display()} - R${self.valor:.2f} em {self.data.strftime('%d/%m/%Y')}"