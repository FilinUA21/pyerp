# Librerias Django
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DeleteView, DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models import PyCompany, PyMeta, PyParameter, PyPlugin, PyWParameter


def _count_plugin():
    return PyPlugin.objects.all().count()


def _web_parameter():
    web_parameter = {}
    for parametro in PyWParameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter


def _parameter():
    parameter = {}
    for parametro in PyParameter.objects.all():
        parameter[parametro.name] = parametro.value
    return parameter


def _web_meta():
    cad = ''
    for meta in PyMeta.objects.all():
        cad += '<meta name="'+meta.title+'" content="'+meta.content+'">' + '\n'
    return cad


# ========================================================================== #
class FatherTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin']= _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        return context

    class Meta:
        abstract = True


# ========================================================================== #
class FatherListView(ListView):
    EXLUDE_FROM_FILTER = (
        'PyCompany',
        'PyCountry',
        'PyCourrency',
        'PyPlugin',
        'PySequence'
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['detail_url'] = '{}:detail'.format(object_name)
        context['add_url'] = '{}:add'.format(object_name)
        return context

    def get_queryset(self):
        if self.model._meta.object_name in self.EXLUDE_FROM_FILTER:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(
                company_id=self.request.user.active_company_id
            )
        return queryset

    class Meta:
        abstract = True


# ========================================================================== #
class FatherDetailView(DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['breadcrumbs'] = [{
            'url': '{}:list'.format(object_name),
            'name': '{}'.format(verbose_name)
        }]
        context['update_url'] = '{}:update'.format(object_name)
        context['delete_url'] = '{}:delete'.format(object_name)
        return context

    class Meta:
        abstract = True


# ========================================================================== #
class FatherCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['breadcrumbs'] = [{
            'url': '{}:list'.format(object_name),
            'name': '{}'.format(verbose_name)
        }]
        context['back_url'] = reverse_lazy('{}:list'.format(object_name))
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.uc = self.request.user.pk
        self.object.company_id = self.request.user.active_company_id
        self.object.save()
        return super().form_valid(form)

    class Meta:
        abstract = True


# ========================================================================== #
class FatherUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['web_parameter'] = _web_parameter()
        context['parameter'] = _parameter()
        context['meta'] = _web_meta()
        context['count_plugin'] = _count_plugin
        context['company'] = PyCompany.objects.filter(active=True)
        context['title'] = '{}'.format(verbose_name)
        context['breadcrumbs'] = [{
            'url': '{}:list'.format(object_name),
            'name': '{}'.format(verbose_name)
        }]
        try:
            context['back_url'] = reverse(
                '{}:detail'.format(object_name),
                kwargs={'pk': context['object'].pk}
            )
        except:
            pass
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.um = self.request.user.pk
        self.object.save()
        return super().form_valid(form)

    class Meta:
        abstract = True


# ========================================================================== #
class FatherDeleteView(DeleteView):
    template_name = 'base/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.model._meta.object_name
        verbose_name = self.model._meta.verbose_name
        context['title'] = _("Delete %(obj_name)s") % {"obj_name": verbose_name}
        context['delete_message'] = _("Are you sure to delete <strong>%(obj_name)s</strong>?") % {"obj_name": verbose_name}
        context['action_url'] = '{}:delete'.format(object_name)
        return context

    def get_success_url(self):
        return '{}:list'.format(self.model._meta.object_name)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy(self.get_success_url())
        eval(self.object.delete())
        return HttpResponseRedirect(success_url)

    class Meta:
        abstract = True
