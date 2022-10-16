import factory

from carford_cars_owners.api.models import Owner, Car


class OwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Owner

    name = 'Michelle Santos'


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    name = 'Fusca'
    color = 'YELLOW'
    model = 'HATCH'
    owner = factory.SubFactory(OwnerFactory)
