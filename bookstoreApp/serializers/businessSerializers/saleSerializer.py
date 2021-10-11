from rest_framework import serializers
from bookstoreApp.models import Sale
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class SaleSerializer(BaseIndepentSerializer): 

    class Meta:
        model= Sale
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer

class SaleUpdateSerializer(SaleSerializer):
    id= serializers.IntegerField()