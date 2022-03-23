import json
from project.tests.base import app, client


def test_get_property_no_filters(client):
    response = client.get('/property/')
    data = json.loads(response.data.decode())
    property = data['data']['properties'][0]
    assert property['address'] == "carrera 100 #15-90"
    assert property['city'] == "barranquilla"
    assert property['price'] == 35000000
    assert property['description'] is None
    assert property['status_id'] == 3
    assert property['year'] == 2015
    assert response.status_code == 200


def test_get_property_filters(client):
    parameters = {
        'status': 3,
        'year': 2020,
        'city': 'bogota'
    }

    response = client.get("/property/", query_string=parameters)

    data = json.loads(response.data.decode())

    assert data['data']['count'] == 2

    property_ = data['data']['properties'][0]

    assert property_['city'] == "bogota"
    assert property_['status_id'] == 3
    assert property_['year'] == 2020
    assert response.status_code == 200


def test_get_property_filters_and_applying_offset(client):
    parameters = {
        'status': 3,
        'year': 2020,
        'city': 'bogota',
        'next': 1
    }

    response = client.get("/property/", query_string=parameters)
    data = json.loads(response.data.decode())

    assert data['data']['count'] == 0
