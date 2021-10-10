#Django rest framework
from rest_framework import serializers


    
    
class BaseProductListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data):  
             
        parent_model_name = self.child.Meta.model.PARENT_MODEL_NAME
        parent_model = self.child.Meta.model.PARENT_MODEL 
         
        model = self.child.Meta.model      
        instances=[]
        for item in validated_data:
            parent_model_data = item.pop(parent_model_name)
            product_instance = parent_model.objects.create(**parent_model_data, )
            instances.append(model(**{parent_model_name: product_instance },**item))         
        return model.objects.bulk_create(instances)

    def update(self, instances_mapping, validated_data):
        
        parent_model_name = self.child.Meta.model.PARENT_MODEL_NAME
        parent_model = self.child.Meta.model.PARENT_MODEL
        
        data_mapping = {item[parent_model_name]['id'] : item for item in validated_data}          
        ret = []                      
        for id, data in data_mapping.items():          
            parent_model_data = data.pop(parent_model_name, None)            
            instance = instances_mapping.get(id, None)                    
            parent_model.objects.filter(id=id).update(**parent_model_data)
            ret.append(instance.update(**data))                        
        return ret

    def to_representation(self, instances):
        instances_representations= []
        for instance in instances:
            instances_representations.append(self.child.to_representation(instance)) 
        return instances_representations

class BaseProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model= None
        fields = '__all__'
        list_serializer_class = BaseProductListSerializer
    
