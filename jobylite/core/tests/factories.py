from factory import DjangoModelFactory
from factory import Faker
from factory import SubFactory

from ..models import Application
from ..models import Job
from ..models import JobContactDetails


class JobContactDetailsFactory(DjangoModelFactory):
    email = Faker("email")
    name = Faker("name")

    class Meta:
        model = JobContactDetails


class JobFactory(DjangoModelFactory):
    title = Faker("name")
    descr = Faker("text")

    class Meta:
        model = Job


class ApplicationFactory(DjangoModelFactory):
    email = Faker("email")
    name = Faker("name")
    job = SubFactory(JobFactory)

    class Meta:
        model = Application
