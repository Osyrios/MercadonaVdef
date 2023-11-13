from flask import url_for


def test_login(client):
    response = client.get(url_for('login.login'))
    assert b'Mercadona - Login' in response.data
