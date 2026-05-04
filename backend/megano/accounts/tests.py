import pytest


@pytest.mark.django_db
def test_logout_user(auth_client):
    response = auth_client.post('/api/sign-out')
    data = response.json()
    assert response.status_code == 200
    assert data == {'message': 'Вы вышли из системы!'}
