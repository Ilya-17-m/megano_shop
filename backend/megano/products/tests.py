import pytest
    
    
@pytest.mark.django_db
def test_get_tags(client, tag):
    response = client.get('/api/tags/')
    data = response.json()

    assert response.status_code == 200
    assert data['results'][0] == {
        'name': 'tech',
        'id': 1
    }


@pytest.mark.django_db
def test_get_product_banner(client, product, review):
    response = client.get('/api/banners/')
    data = response.json()
    assert response.status_code == 200
    assert data == {

    }