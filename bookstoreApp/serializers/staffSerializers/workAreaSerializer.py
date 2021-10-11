from rest_framework import serializers
from bookstoreApp.models import WorkArea
from .. import BaseIndepentSerializer, BaseIndepentListSerializer


class WorkAreaSerializer(BaseIndepentSerializer): 

    class Meta:
        model= WorkArea
        fields = ['id','name']
        list_serializer_class = BaseIndepentListSerializer

class WorkAreaUpdateSerializer(WorkAreaSerializer):
    id= serializers.IntegerField()
    name = serializers.CharField()