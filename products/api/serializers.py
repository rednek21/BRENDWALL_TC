from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description']

    def validate_title(self, value):
        if not value.strip():
            raise ValidationError("Название продукта не должно быть пустым")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Цена продукта должна быть положительной")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise ValidationError("Описание продукта не должно быть пустым")
        return value
