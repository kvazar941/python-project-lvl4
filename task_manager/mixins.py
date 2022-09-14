from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy

from task_manager.app_tasks.models import Tasks


class CheckSignInMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class CheckDeleteMixin(AccessMixin):
    error_delete_message = ''
    success_delete_message = ''
    redirect_delete_url = ''
    success_url = ''

    def form_valid(self, request, *args, **kwargs):
        if Tasks.objects.filter(status=self.get_object().pk):
            messages.error(
                self.request,
                gettext_lazy(self.error_delete_message),
            )
            return HttpResponseRedirect(
                reverse_lazy(self.redirect_delete_url),
            )
        messages.success(
            self.request,
            gettext_lazy(self.success_delete_message),
        )
        return super().delete(request, *args, **kwargs)
