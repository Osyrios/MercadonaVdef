from flask import url_for


def test_logout(client):
    response = client.post(url_for('logout.logout'), follow_redirects=True)
    assert b'Mercadona - Catalogue' in response.data
