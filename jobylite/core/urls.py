from django.urls import path

from .views import job_contact_details_create_view
from .views import job_create_view
from .views import index_view

app_name = "core"
urlpatterns = [
    path("", view=index_view, name="index"),
    path("jobs/create/", view=job_create_view, name="job-create"),
    path(
        "hiring-manager/create/",
        view=job_contact_details_create_view,
        name="contact-details-create",
    ),
]
