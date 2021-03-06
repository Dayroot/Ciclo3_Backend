from rest_framework import serializers
from bookstoreApp.models import ShoppingCart
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class ShoppingCartSerializer(BaseIndepentSerializer): 
    
    class Meta:
        model= ShoppingCart
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer
    
    def to_representation(self, instance):
        return {
                "Customer_id": instance.customer.id,
                "shoppingCart_id": instance.id            
        }

class ShoppingCartUpdateSerializer(ShoppingCartSerializer):
    id = serializers.IntegerField()
    