from flask import url_for


def test_homepage(client):
    response = client.get(url_for('homepage.homepage'))
    assert b'Mercadona - Homepage' in response.data
