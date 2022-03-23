import pytest
from project.server.models import Property
from project.server.orm import Condition
from project.tests.base import app


def test_get_property():
    p = Property.objects.select("address", condition=Condition(id=1))
    assert p[0].address == "calle 23 #45-67"


def test_get_property_attribute_not_present():
    p = Property.objects.select("address", condition=Condition(id=1))
    with pytest.raises(AttributeError):
        p[0].age


def test_get_property_custom_query():
    p = Property.objects.execute_custom_query("SELECT * FROM property LIMIT 2")
    assert p[0].address == "calle 23 #45-67"
