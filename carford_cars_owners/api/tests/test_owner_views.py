import json

import pytest

from django.test import Client

pytestmark = [pytest.mark.django_db]


def test_must_create_owner(client: Client):
    data_requests = {
        "name": "Michelle Santos"
    }

    response = client.post(path='/api/v1/owners/', data=data_requests)

    assert response.status_code == 201
    data_response = json.loads(response.content)
    assert data_response['name'] == 'Michelle Santos'
    assert data_response['sale_opportunity'] is True


def test_must_list_owners(client: Client, owner):

    response = client.get(path='/api/v1/owners/')

    assert response.status_code == 200

    data_response = json.loads(response.content)[0]
    assert data_response['name'] == owner.name
    assert data_response['sale_opportunity'] is owner.sale_opportunity
