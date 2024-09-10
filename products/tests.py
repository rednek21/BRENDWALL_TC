from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from .models import Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_product():
    def _create_product(title, price, description):
        return Product.objects.create(title=title, price=price, description=description)
    return _create_product

@pytest.fixture
def product_data():
    return {
        "title": "Test Product",
        "price": 100.0,
        "description": "A test product"
    }

@pytest.mark.django_db
def test_create_product(api_client, product_data):
    url = reverse('product-create-list')
    response = api_client.post(url, data=product_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": "Продукт успешно создан"}
    assert Product.objects.count() == 1
    assert Product.objects.first().title == "Test Product"

@pytest.mark.django_db
def test_create_product_invalid_data(api_client):
    url = reverse('product-create-list')
    response = api_client.post(url, data={})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'errors' in response.json()

@pytest.mark.django_db
def test_list_products(api_client, create_product):
    create_product("Product 1", 50.0, "First product")
    create_product("Product 2", 150.0, "Second product")
    create_product("Product 3", 200.0, "Third product")

    url = reverse('product-list-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3
    assert response.json()[0]['title'] == "Product 3"
    assert response.json()[1]['title'] == "Product 2"
    assert response.json()[2]['title'] == "Product 1"