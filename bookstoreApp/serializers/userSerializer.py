from django.db.models import fields
from bookstoreApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username', 'password']