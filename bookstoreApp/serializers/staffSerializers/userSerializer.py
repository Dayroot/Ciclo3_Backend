from bookstoreApp.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields= '__all__'
        
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
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return instance.update(**validated_data)
class UserUpdateSerializer(UserSerializer):
    
    username= serializers.CharField()
    id= serializers.IntegerField()

        