from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .forms import JobContactDetailsForm
from .forms import JobForm
from .models import Job


class IndexView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = "jobs"


class JobCreateView(LoginRequiredMixin, CreateView):
    template_name = "core/job_form.html"
    form_class = JobForm
    success_url = "/"


class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/job_detail.html"
    model = Job
    context_object_name = "job"


class JobContactDetailsCreateView(LoginRequiredMixin, CreateView):
    template_name = "core/contact_details_form.html"
    form_class = JobContactDetailsForm
    success_url = "/"


index_view = IndexView.as_view()
job_create_view = JobCreateView.as_view()
job_detail_view = JobDetailView.as_view()
job_contact_details_create_view = JobContactDetailsCreateView.as_view()
