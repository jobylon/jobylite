import pytest

from django.conf import settings
from django.urls import resolve
from django.urls import reverse


def test_index():
    assert reverse("core:index") == f"/"
    assert resolve(f"/").view_name == "core:index"
