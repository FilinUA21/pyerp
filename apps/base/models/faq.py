# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather


class PyFaq(PyFather):
    name = models.CharField(_("Name"), max_length=40)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('base:faq-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name