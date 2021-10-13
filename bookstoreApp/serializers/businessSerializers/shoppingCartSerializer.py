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
                "Datetime": instance.datetime,
                "Customer fullname": instance.customer.fullname,
                "Customer identification": instance.customer.identification            
        }

class ShoppingCartUpdateSerializer(ShoppingCartSerializer):
    id = serializers.IntegerField()
    