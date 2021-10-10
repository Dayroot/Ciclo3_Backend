from django.db.models import fields
from rest_framework import serializers
from bookstoreApp.models.workArea import WorkArea
from bookstoreApp.models.employee import Employee


class WorkAreaListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data): 
        workAreas=[]
        for item in validated_data:            
            workAreas.append(self.child.create(item))   
        return WorkArea.objects.bulk_create(workAreas)
    
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        workArea_mapping = {workArea.id: workArea for workArea in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for workArea_id, data in data_mapping.items():
            workArea = workArea_mapping.get(workArea_id, None)
            if workArea is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(workArea, data))

        # Perform deletions.
        for workArea_id, workArea in workArea_mapping.items():
            if workArea_id not in data_mapping:
                workArea.delete()
                
        return ret

    def to_representation(self, instance):
        workArea_representations= []
        for workArea in instance:
            workArea_representations.append(self.child.to_representation(workArea)) 
        return workArea_representations
    

class WorkAreaSerializer(serializers.ModelSerializer):  
    class Meta:
        model= WorkArea
        fields = '__all__'
        list_serializer_class = WorkAreaListSerializer

    def create(self, validated_data):       
        return WorkArea(**validated_data)