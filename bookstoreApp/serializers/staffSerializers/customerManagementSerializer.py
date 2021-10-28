from rest_framework import serializers
from bookstoreApp.models import User, ShoppingCart
from .. import BaseIndepentSerializer

class CustomerListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data): 
        instances=[]
        for item in validated_data:            
            instances.append(self.child.create(item))   
        return instances
    
    def update(self, instances_mapping, validated_data):
        data_mapping = {item['id']: item for item in validated_data}
        ret = []
        for id, data in data_mapping.items():
            instance = instances_mapping.get(id, None)
            ret.append(instance.update(**data))
        # Perform deletions.
        for id, instance in instances_mapping.items():
            if id not in data_mapping:
                instance.delete()
                
        return ret

    def to_representation(self, instances):
        instances_representations= []
        for instance in instances:
            instances_representations.append(self.child.to_representation(instance)) 
        return instances_representations
    


class CustomerManagementSerializer(BaseIndepentSerializer): 

    class Meta:
        model= User
        fields = '__all__'
        list_serializer_class = CustomerListSerializer
        
    def to_representation(self, instance):
        return {
                    'id':instance.id,
                    'username': instance.username,
                    'fullname': instance.fullname,
                    'datebirth': instance.datebirth,
                    'gender':instance.gender,
                    'email': instance.email,
                    'identification': instance.identification,
                    'phone_number':instance.phone_number,
                    'address': instance.address    
                }
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if validated_data["is_customer"] == True:
            shopping_cart = ShoppingCart.objects.create(customer_id=user.id)
        return user

class CustomerManagementUpdateSerializer(CustomerManagementSerializer):
    username= serializers.CharField()
    id= serializers.IntegerField()