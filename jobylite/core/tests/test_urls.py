from django.urls import resolve
from django.urls import reverse


def test_index():
    assert reverse("core:index") == f"/"
    assert resolve(f"/").view_name == "core:index"


def test_job_create():
    assert reverse("core:job-create") == f"/jobs/create/"
    assert resolve(f"/jobs/create/").view_name == "core:job-create"


def test_job_detail():
    assert reverse("core:job-detail", kwargs={"pk": 1}) == f"/jobs/1/"
    assert resolve(f"/jobs/1/").view_name == "core:job-detail"
    assert resolve(f"/jobs/1/").kwargs == {"pk": 1}


def test_contact_details_create():
    assert reverse("core:contact-details-create") == f"/hiring-manager/create/"
    assert (
        resolve(f"/hiring-manager/create/").view_name == "core:contact-details-create"
    )
