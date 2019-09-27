# Librerias Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from ..models import PyAttribute, PyLog
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

ATTRIBUTE_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Variant"), 'field': 'variant_id'},
]

ATTRIBUTE_SHORT = ['name','variant_id']


class AttributeListView(LoginRequiredMixin, FatherListView):
    model = PyAttribute
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeListView, self).get_context_data(**kwargs)
        context['title'] = 'Attribute'
        context['detail_url'] = 'base:attribute-detail'
        context['add_url'] = 'base:attribute-add'
        context['fields'] = ATTRIBUTE_FIELDS
        return context


class AttributeDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyAttribute
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:attributes', 'name': 'Attribute'}]
        context['update_url'] = 'base:attribute-update'
        context['delete_url'] = 'base:attribute-delete'
        context['fields'] = ATTRIBUTE_FIELDS
        return context


class AttributeCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyAttribute
    fields = ATTRIBUTE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Attribute'
        context['breadcrumbs'] = [{'url': 'base:attributes', 'name': 'Attributes'}]
        context['back_url'] = reverse('base:attributes')
        return context


class AttributeUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyAttribute
    fields = ATTRIBUTE_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(AttributeUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:attributes', 'name': 'Attributes'}]
        context['back_url'] = reverse('base:attribute-detail', kwargs={'pk': context['object'].pk})
        return context


class AttributeDeleteView(FatherDeleteView):
    model = PyAttribute
    success_url = 'base:attributes'
