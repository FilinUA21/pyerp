"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.attribute import (
    AttributeCreateView, AttributeDeleteView, AttributeDetailView,
    AttributeListView, AttributeUpdateView)

app_name = 'PyAttribute'

urlpatterns = [
    path('', AttributeListView.as_view(), name='list'),
    path('add/', AttributeCreateView.as_view(), name='add'),
    path('<int:pk>/', AttributeDetailView.as_view(), name='detail'),
    path('<int:pk>/update', AttributeUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AttributeDeleteView.as_view(), name='delete'),
]
