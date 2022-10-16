from pytest_factoryboy import register

from carford_cars_owners.api.factories import OwnerFactory, CarFactory


register(OwnerFactory)
register(CarFactory)
