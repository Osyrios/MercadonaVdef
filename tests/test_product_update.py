from flask import url_for


def test_product_update(client):
    product_id = 1
    with client.session_transaction() as session:
        session['user'] = 'admin'
    response = client.get(url_for('product_update.product_update', product_id=product_id), follow_redirects=True)

    # Vérifiez que la réponse contient les informations attendues dans le template
    assert b'Mercadona - Modifier un produit' in response.data
    assert b'name' in response.data
    assert b'description' in response.data
    assert b'image_data' in response.data
    assert b'price' in response.data