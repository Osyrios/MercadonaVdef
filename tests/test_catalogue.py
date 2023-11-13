from flask import url_for


def test_catalogue(client):
    response = client.get(url_for('catalogue.catalogue'))
    assert b'Mercadona - Catalogue' in response.data
