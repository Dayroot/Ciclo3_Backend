from rest_framework import serializers



class BaseIndepentListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data): 
        instances=[]
        for item in validated_data:            
            instances.append(self.child.create(item))   
        return self.child.Meta.model.objects.bulk_create(instances)
    
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
    

class BaseIndepentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= None
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer

    def create(self, validated_data):       
        return self.Meta.model(**validated_data)
           

        

