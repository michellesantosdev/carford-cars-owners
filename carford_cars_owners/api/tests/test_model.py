import pytest

from carford_cars_owners.api.models import Car, Owner

pytestmark = [pytest.mark.django_db]


def test_must_create_car(car, owner):
    assert Car.objects.count() == 1
    assert car.name == 'Fusca'
    assert car.color == 'YELLOW'
    assert car.model == 'HATCH'
    assert car.owner == owner


def test_must_create_owner(owner):
    assert Owner.objects.count() == 1
    assert owner.name == 'Michelle Santos'
