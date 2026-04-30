import pytest


@pytest.mark.django_db
def test_get_order(auth_client, order_rel_with_tables):
    response = auth_client.get('/api/orders/')
    data = response.json()
    assert response.status_code == 200
    print(data)
