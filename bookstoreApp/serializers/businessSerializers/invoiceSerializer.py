from rest_framework import serializers
from bookstoreApp.models import Invoice
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class InvoiceSerializer(BaseIndepentSerializer): 
    
    class Meta:
        model= Invoice
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer
    
    def to_representation(self, instance):
        return {
                "invoice_id": instance.id,
                "Customer_id": instance.customer.id,
                "datetime": instance.datetime            
        }

class InvoiceUpdateSerializer(InvoiceSerializer):
    id = serializers.IntegerField()
    