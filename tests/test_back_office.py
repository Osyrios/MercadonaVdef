from flask import url_for


def test_back_office(client):
    response = client.get(url_for('back_office.back_office'), follow_redirects=True)
    assert b'Mercadona - Login' in response.data
