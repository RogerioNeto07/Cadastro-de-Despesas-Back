from django.urls import path
from .views import DespesaListView, DespesaDetailView

urlpatterns = [
    path('despesas/', DespesaListView.as_view(), name='despesa-list-create'),
    path('despesas/<int:pk>/', DespesaDetailView.as_view(), name='despesa-detail'),
]