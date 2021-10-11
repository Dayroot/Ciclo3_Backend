from rest_framework import serializers
from bookstoreApp.models import Reservation
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class ReservationSerializer(BaseIndepentSerializer): 

    class Meta:
        model= Reservation
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer

class ReservationUpdateSerializer(ReservationSerializer):
    id= serializers.IntegerField()