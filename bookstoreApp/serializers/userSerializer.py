from django.db.models import fields
from bookstoreApp.models.user import User
from rest_framework import serializers
from rest_framework.fields import empty

class UserSerializer(serializers.ModelSerializer):
    username= serializers.CharField()
    class Meta:
        model = User
        fields= '__all__'
        
