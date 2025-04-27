from django.db import models

class Despesa(models.Model):
    CATEGORIAS = [
        ('LAZER', 'Lazer'),
        ('CONTAS', 'Contas'),
        ('MERCADO', 'Mercado'),
        ('SAUDE', 'Saúde'),
        ('COMIDA', 'Comida'),
    ]

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='CONTAS'
    )
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return f"{self.get_categoria_display()} - R${self.valor} em {self.data}"
    
    def is_grande_gasto(self):
        '''Retorna true se o valor da despesa é maior ou igual a 100 reais'''
        return self.valor >= 100
    
    def is_economizavel(self):
        '''Retorna True se a despesa for da categoria Lazer ou Comida.'''
        return self.categoria in ['LAZER', 'COMIDA']
    
