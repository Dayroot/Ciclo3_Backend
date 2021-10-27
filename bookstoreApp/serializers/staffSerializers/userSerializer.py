from bookstoreApp.models import User, ShoppingCart
from rest_framework import serializers
from .. import BaseIndepentSerializer, BaseIndepentListSerializer


class UserSerializer(BaseIndepentSerializer):
    
    class Meta:
        model = User
        fields= '__all__'
        list_serializer_class = BaseIndepentListSerializer
        
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
    
    def update(self, instance, validated_data):
        return instance.update(**validated_data)
class UserUpdateSerializer(UserSerializer):
    
    username= serializers.CharField()
    id= serializers.IntegerField()

        