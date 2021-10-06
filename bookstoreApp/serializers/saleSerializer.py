from django.db.models import fields
from rest_framework import serializers
from bookstoreApp.models.sale import Sale
from bookstoreApp.models.user import User
from bookstoreApp.models.product import Product


class SaleListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data): 
        sales=[]
        for item in validated_data:            
            sales.append(Sale(**item))   
        return Sale.objects.bulk_create(sales)
    
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        sale_mapping = {sale.id: sale for sale in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for sale_id, data in data_mapping.items():
            sale = sale_mapping.get(sale_id, None)
            if sale is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(sale, data))

        # Perform deletions.
        for sale_id, sale in sale_mapping.items():
            if sale_id not in data_mapping:
                sale.delete()
                
        return ret

    def to_representation(self, instance):
        sale_representations= []
        for sale in instance:
            sale_representations.append({   
                'id': sale.product_id,
                'quantity':sale.quantity,
                'product_id':sale.product_id,
                'user_id':sale.user_id,
                }) 
        return sale_representations

class SaleSerializer(serializers.ModelSerializer):  
    class Meta:
        model= Sale
        fields = '__all__'
        list_serializer_class = SaleListSerializer