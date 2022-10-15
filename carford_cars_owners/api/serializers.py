from rest_framework import serializers

from carford_cars_owners.api.models import Owner, Car


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'
        read_only_fields = ['sale_opportunity']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

    def validate_owner(self, value):
        cars = Car.objects.filter(owner=value.id)
        if len(cars) > 3:
            raise serializers.ValidationError("One owner can have up to 3 vehicles.")

        return value
