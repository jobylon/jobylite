from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .models import Job


class IndexView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = "jobs"


index_view = IndexView.as_view()
