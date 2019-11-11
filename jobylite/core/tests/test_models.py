import pytest

from ..models import Application
from ..models import Job
from ..models import JobContactDetails

pytestmark = pytest.mark.django_db


def test_application_str(application: Application):
    assert str(application) == f"{application.name}: {application.email}"


def test_application_repr(application: Application):
    assert (
        repr(application)
        == f"{application.__class__.__name__}({application.id}, {application.name})"
    )


def test_job_str(job: Job):
    assert str(job) == f"{job.title}"


def test_job_repr(job: Job):
    assert repr(job) == f"{job.__class__.__name__}({job.id}, {job.title})"


def test_job_contact_details_str(job_contact_details: JobContactDetails):
    assert (
        str(job_contact_details)
        == f"{job_contact_details.name}: {job_contact_details.email}"
    )


def test_job_contact_details_repr(job_contact_details: JobContactDetails):
    assert (
        repr(job_contact_details)
        == f"{job_contact_details.__class__.__name__}({job_contact_details.id}, {job_contact_details.name}, {job_contact_details.email})"
    )
