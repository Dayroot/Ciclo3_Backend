from rest_framework import serializers
from bookstoreApp.models.workArea import WorkArea
from .baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer


class WorkAreaSerializer(BaseIndepentSerializer): 

    class Meta:
        model= WorkArea
        fields = ['id','name']
        list_serializer_class = BaseIndepentListSerializer

class WorkAreaUpdateSerializer(WorkAreaSerializer):
    id= serializers.IntegerField()
    name = serializers.CharField()