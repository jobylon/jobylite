from django import forms

from .models import Job
from .models import JobContactDetails


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("title", "descr", "contact_details")


class JobContactDetailsForm(forms.ModelForm):
    class Meta:
        model = JobContactDetails
        fields = ("email", "name", "phone")
