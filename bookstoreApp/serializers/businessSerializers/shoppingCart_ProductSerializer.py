from rest_framework import serializers
from bookstoreApp.models import ShoppingCart_Product
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class ShoppingCart_ProductSerializer(BaseIndepentSerializer): 
    
    class Meta:
        model= ShoppingCart_Product
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer
    
    def to_representation(self, instance):
        return {
                "Description": instance.product.description,
                "Quantity": instance.quantity,
                "Price by unit": instance.product.price,
                "Total": instance.quantity*instance.product.price,
          
        }

class ShoppingCart_ProductUpdateSerializer(ShoppingCart_ProductSerializer):
    id = serializers.IntegerField()
    