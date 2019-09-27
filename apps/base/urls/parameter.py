"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.parameter import (
    ParameterCreateView, ParameterDeleteView, ParameterDetailView,
    ParameterListView, ParameterUpdateView)

app_name = 'PyParameter'

urlpatterns = [
    path('', ParameterListView.as_view(), name='list'),
    path('add/', ParameterCreateView.as_view(), name='add'),
    path('<int:pk>/', ParameterDetailView.as_view(), name='detail'),
    path('<int:pk>/update', ParameterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ParameterDeleteView.as_view(), name='delete'),
]
