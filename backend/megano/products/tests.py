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
def test_get_product_banner(client, product_rel_with_tables):
    response = client.get('/api/banners/')
    data = response.json()
    assert response.status_code == 200
    assert data == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {'id': 1,
             'category': 0,
             'price': 2000,
             'count': 1,
             'date': '24.04.2026',
             'title': 'MacBook',
             'description': 'great',
             'freeDelivery': True,
             'images': [1],
             'tags': [1],
             'rating': 3,
             'reviews':
                 []
             }
        ]
    }


@pytest.mark.django_db
def test_get_limited_product(client, product_rel_with_tables):
    response = client.get('/api/products/limited/')
    data = response.json()
    assert response.status_code == 200
    assert data == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': 1,
                'category': 0,
                'price': 2000,
                'count': 1,
                'date': '24.04.2026',
                'title': 'MacBook',
                'description': 'great',
                'fullDescription': 'I like this product',
                'freeDelivery': True,
                'images': [
                    {'src': None,
                     'alt': 'image'}
                ],
                'tags': [
                    {'id': 1,
                     'name': 'tech'}
                ],
                'rating': 3,
                'specifications': [
                    {'id': 1,
                     'name': 'size',
                     'value': '16x9'}
                ],
                'reviews': []
            }
        ]
    }


@pytest.mark.django_db
def test_get_popular_product(client, product_rel_with_tables):
    response = client.get('/api/products/popular/')
    data = response.json()
    assert response.status_code == 200
    assert data == {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'id': 1,
                'category': 0,
                'price': 2000,
                'count': 1,
                'date': '24.04.2026',
                'title': 'MacBook',
                'description': 'great',
                'fullDescription': 'I like this product',
                'freeDelivery': True,
                'images': [
                    {'src': None,
                     'alt': 'image'}
                ], 'tags': [
                {'id': 1,
                 'name': 'tech'
                 }],
                'rating': 3,
                'specifications': [
                    {'id': 1,
                     'name': 'size',
                     'value': '16x9'}
                ], 'reviews': []
            }
        ]
    }


@pytest.mark.django_db
def test_get_product_detail(client, product_rel_with_tables):
    response = client.get('/api/product/1/')
    data = response.json()
    assert response.status_code == 200
    assert data == {
        'id': 1,
        'category': 0,
        'price': 2000,
        'count': 1,
        'date': '24.04.2026',
        'title': 'MacBook',
        'description': 'great',
        'fullDescription': 'I like this product',
        'freeDelivery': True,
        'images': [
            {'src': None,
             'alt': 'image'}
        ],
        'tags': [
            {'id': 1,
             'name': 'tech'}
        ], 'rating': 3,
        'specifications': [
            {'id': 1,
             'name': 'size',
             'value': '16x9'}
        ], 'reviews': []
    }


@pytest.mark.django_db
def test_get_sales_product(client, product_rel_with_tables):
    response = client.get('/api/sales/')
    data = response.json()
    assert response.status_code == 200
    assert data == {'items': [], 'currentPage': 1, 'lastPage': 1}


