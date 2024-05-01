import pytest
from app import *

@pytest.fixture
def test_client():
    with app.test_client() as client:
        with app.app_context():
            # Configuration pour chaque test
            db.create_all()
            yield client  # Fournir le client de test
            # Nettoyage après chaque test
            db.drop_all()

# Test de la route /identify
def test_identify(test_client):
    response = test_client.post('/identify', data={'image': (io.BytesIO(b'some-image-data'), 'depositphotos_258709504-stock-photo-large-dog-footprint-fresh-imprint.jpg')})
    assert response.status_code == 200
    assert 'animal' in response.json
