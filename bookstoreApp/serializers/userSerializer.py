from bookstoreApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'fullname', 
            'datebirth',
            'email',
            'identification',
            'phone_number',
            'address',
            'is_employee',
            'is_client'
            ]