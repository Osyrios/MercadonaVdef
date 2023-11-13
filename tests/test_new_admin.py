from flask import url_for


def test_new_admin(client):
    with client.session_transaction() as session:
        session['user'] = 'admin'
    response = client.get(url_for('new_admin.new_admin'), follow_redirects=True)
    assert b'Mercadona - Nouvel utilisateur' in response.data
