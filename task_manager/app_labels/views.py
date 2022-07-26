from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from task_manager.app_labels.forms import LabelForm
from task_manager.app_labels.models import Label
from task_manager.mixins import CheckDeleteMixin, CheckSignInMixin


class ListOfLabels(CheckSignInMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class CreateLabel(SuccessMessageMixin, CheckSignInMixin, CreateView):
    model = Label
    template_name = 'labels/labels_create.html'
    form_class = LabelForm
    success_message = _('Label created successfully')
    success_url = reverse_lazy('list_of_labels')


class UpdateLabel(CheckSignInMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'labels/labels_update.html'
    form_class = LabelForm
    success_message = _('Label changed successfully')
    success_url = reverse_lazy('list_of_labels')


class DeleteLabel(CheckSignInMixin, CheckDeleteMixin, SuccessMessageMixin):
    model = Label
    template_name = 'labels/labels_delete.html'
    error_delete_message = _("Can't delete label because it's in use")
    success_delete_message = _('Label deleted successfully')
    redirect_delete_url = reverse_lazy('list_of_labels')
    success_url = reverse_lazy('list_of_labels')
