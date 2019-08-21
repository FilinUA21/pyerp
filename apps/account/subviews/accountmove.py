from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from ..submodels.accountmove import PyAccountMove

ACCOUNTMOVE_FIELDS = [
            {'string': 'Código', 'field': 'code'},
            {'string': 'Nombre', 'field': 'name'},
            {'string': 'Estado', 'field': 'state'},
        ]

ACCOUNTMOVE_FIELDS_SHORT = ['code','name','state']


class AccountMoveListView(ListView):
    model = PyAccountMove
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveListView, self).get_context_data(**kwargs)
        context['title'] = 'Asiento Contable'
        context['detail_url'] = 'accountmove-detail'
        context['add_url'] = 'accountmove-add'
        context['fields'] = ACCOUNTMOVE_FIELDS
        return context

class AccountMoveDetailView(DetailView):
    model = PyAccountMove
    template_name = 'erp/detail.html'
    def get_context_data(self, **kwargs):
        context = super(AccountMoveDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'accountmove', 'name': 'Asiento Contable'}]
        context['update_url'] = 'accountmove-update'
        context['delete_url'] = 'accountmove-delete'
        context['fields'] = ACCOUNTMOVE_FIELDS
        return context

class AccountMoveCreateView(CreateView):
    model = PyAccountMove
    fields = ACCOUNTMOVE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Asiento'
        context['breadcrumbs'] = [{'url': 'accountmove', 'name': 'Crear Asiento'}]
        context['back_url'] = reverse('accountmove')
        return context

class AccountMoveUpdateView(UpdateView):
    model = PyAccountMove
    fields = ACCOUNTMOVE_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMoveUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'accountmove', 'name': 'Asiento Contable'}]
        context['back_url'] = reverse('accountmove-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteAccountMove(self, pk):
    accountmove = PyAccountMove.objects.get(id=pk)
    accountmove.delete()
    return redirect(reverse('accountmove'))