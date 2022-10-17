from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.response import Response
from rest_framework import status
from carford_cars_owners.api.models import Owner, Car
from carford_cars_owners.api.serializers import OwnerSerializer, CarSerializer


class OwnersViews(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarsViews(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        owner = Owner.objects.get(pk=serializer.validated_data['owner'].id)
        owner.sale_opportunity = False
        owner.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
