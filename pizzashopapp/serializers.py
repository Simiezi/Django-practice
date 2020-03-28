from rest_framework import serializers
from pizzashopapp.models import PizzaShop


class PizzaShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, max_length=100, allow_blank=True)
    phone = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    logo = serializers.ImageField(upload_to='pizzashop_logo/', blank=False)
