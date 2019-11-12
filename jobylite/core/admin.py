from django.contrib import admin

from .models import Application
from .models import Job
from .models import JobContactDetails


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name", "email")
    raw_id_fields = ("job",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "dt_created")
    search_fields = ("title",)
    raw_id_fields = ("contact_details",)


@admin.register(JobContactDetails)
class JobContactDetailsAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name", "email")
