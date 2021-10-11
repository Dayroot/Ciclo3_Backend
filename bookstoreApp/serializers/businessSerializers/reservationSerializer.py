from rest_framework import serializers
from bookstoreApp.models import Reservation
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class ReservationSerializer(BaseIndepentSerializer): 
    
    class Meta:
        model= Reservation
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer
    
    def to_representation(self, instance):
        return {
                "Description": instance.product.description,
                "Quantity": instance.quantity,
                "Price by unit": instance.product.price,
                "Total": instance.quantity*instance.product.price,
                "Datetime": instance.datetime,
                "Customer fullname": instance.customer.fullname,
                "Customer identification": instance.customer.identification            
        }

class ReservationUpdateSerializer(ReservationSerializer):
    id = serializers.IntegerField()
    