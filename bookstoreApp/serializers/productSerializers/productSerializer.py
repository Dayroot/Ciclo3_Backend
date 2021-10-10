from rest_framework import serializers
from bookstoreApp.models import Product


class ProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model= Product
        fields = '__all__'
        

class ProductUpdateSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField()
    class Meta:
        model = Product
        fields= '__all__'
        