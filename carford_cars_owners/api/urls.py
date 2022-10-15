from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter

from carford_cars_owners.api.views import OwnersViews, CarsViews


owners_routers = DefaultRouter()
owners_routers.register('owners', OwnersViews, basename='OwnersViews')

cars_routers = DefaultRouter()
cars_routers.register('cars', CarsViews, basename='CarsViews')

app_name = 'api'

urlpatterns = (
    path('', include(owners_routers.urls)),
    path('', include(cars_routers.urls)),
)
