from factory import DjangoModelFactory
from factory import Faker

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
