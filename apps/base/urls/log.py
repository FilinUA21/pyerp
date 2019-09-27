"""uRLs para base
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.log import (
    LogCreateView, LogDeleteView, LogDetailView, LogListView, LogUpdateView)

app_name = 'PyLog'

urlpatterns = [
    path('', LogListView.as_view(), name='list'),
    path('add/', LogCreateView.as_view(), name='add'),
    path('<int:pk>/', LogDetailView.as_view(), name='detail'),
    path('<int:pk>/update', LogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', LogDeleteView.as_view(), name='delete'),
]
