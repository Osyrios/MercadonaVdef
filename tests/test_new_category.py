from flask import url_for


def test_new_category(client):
    with client.session_transaction() as session:
        session["user"] = "admin"
    response = client.get(url_for('new_category.new_category'), follow_redirects=True)
    assert b'Mercadona - Nouvelle categorie' in response.data
