import pytest
from django.conf import settings
from django.test import RequestFactory

from jobylite.core.models import Application
from jobylite.core.models import Job
from jobylite.core.models import JobContactDetails
from jobylite.core.tests.factories import ApplicationFactory
from jobylite.core.tests.factories import JobFactory
from jobylite.core.tests.factories import JobContactDetailsFactory
from jobylite.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def application() -> Application:
    return ApplicationFactory()


@pytest.fixture
def job() -> Job:
    return JobFactory()


@pytest.fixture
def job_contact_details() -> JobContactDetails:
    return JobContactDetailsFactory()
