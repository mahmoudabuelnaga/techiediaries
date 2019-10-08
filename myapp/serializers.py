from rest_framework import serializers
from .models import Product, Family, Location, Transaction

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("reference","title","description")

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    family = FamilySerializer()
    location = LocationSerializer()
    class Meta:
        model = Product
        fields = ("sku","barcode","title","description","family","location")

class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Transaction
        fields = ("sku", "barcode","product")