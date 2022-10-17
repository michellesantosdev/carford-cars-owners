import json

import pytest

from django.test import Client

pytestmark = [pytest.mark.django_db]


def test_must_car_owner(client: Client, owner):
    data_requests = {
        'name': 'Fusca',
        'color': 'YELLOW',
        'model': 'HATCH',
        'owner': owner.id
    }

    response = client.post(path='/api/v1/cars/', data=data_requests)

    assert response.status_code == 201
    data_response = json.loads(response.content)
    assert data_response == {
        'id': 1,
        'name': 'Fusca',
        'color': 'YELLOW',
        'model': 'HATCH',
        'owner': 1
    }


def test_must_list_cars(client: Client, car):

    response = client.get(path='/api/v1/cars/')

    assert response.status_code == 200

    data_response = json.loads(response.content)[0]
    assert data_response['name'] == car.name
    assert data_response['color'] == car.color
    assert data_response['model'] == car.model
    assert data_response['owner'] == car.owner.id


def test_should_not_create_car_with_color_and_model_different_from_the_choices(client: Client, owner):
    data_requests = {
        'name': 'Fusca',
        'color': 'PRETO',
        'model': 'VELHO',
        'owner': owner.id
    }

    response = client.post(path='/api/v1/cars/', data=data_requests)

    assert response.status_code == 400

    data_response = json.loads(response.content)
    assert data_response == {
        'color': ['"PRETO" is not a valid choice.'],
        'model': ['"VELHO" is not a valid choice.']
    }


def test_should_not_create_car_without_owner(client: Client):
    data_requests = {
        'name': 'Fusca',
        'color': 'YELLOW',
        'model': 'HATCH'
    }

    response = client.post(path='/api/v1/cars/', data=data_requests)

    assert response.status_code == 400

    data_response = json.loads(response.content)
    assert data_response == {
        'owner': ['This field is required.']
    }


def test_should_mark_owner_without_car_sales_opportunity(client: Client, owner):
    assert owner.sale_opportunity is True

    data_requests_car = {
        'name': 'Fusca',
        'color': 'YELLOW',
        'model': 'HATCH',
        'owner': owner.id
    }
    response = client.post(path='/api/v1/cars/', data=data_requests_car)
    assert response.status_code == 201

    response = client.get(path=f'/api/v1/owners/{owner.id}/')
    assert response.status_code == 200
    data_response = json.loads(response.content)
    assert data_response == {
        'id': owner.id,
        'name': 'Michelle Santos',
        'sale_opportunity': False
    }


def test_should_not_create_for_owner_with_more_than_3_vehicles(client: Client):
    data_requests_owner_without_car = {
        "name": "Michelle Santos"
    }
    response_owner = client.post(path='/api/v1/owners/', data=data_requests_owner_without_car)
    data_response_owner = json.loads(response_owner.content)
    owner_id = data_response_owner['id']

    data_requests_car = {
        'name': 'Fusca',
        'color': 'YELLOW',
        'model': 'HATCH',
        'owner': owner_id
    }
    for i in range(0, 4):
        response_car = client.post(path='/api/v1/cars/', data=data_requests_car)
        assert response_car.status_code == 201

    response_car_error = client.post(path='/api/v1/cars/', data=data_requests_car)
    assert response_car_error.status_code == 400
    data_response_car_error = json.loads(response_car_error.content)
    assert data_response_car_error == {
        'owner': ['One owner can have up to 3 vehicles.']
    }
