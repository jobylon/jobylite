from django.db import models

from jobylite.utils.models import TimeStampedModel


class Application(TimeStampedModel):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    job = models.ForeignKey("Job", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.email}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name})"


class Job(TimeStampedModel):

    title = models.CharField(max_length=250)
    descr = models.TextField()
    skills = models.TextField(blank=True, null=True)
    contact_details = models.ForeignKey(
        "JobContactDetails", on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.title})"


class JobContactDetails(TimeStampedModel):

    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.email}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name}, {self.email})"

    class Meta:
        verbose_name_plural = "Job contact details"
