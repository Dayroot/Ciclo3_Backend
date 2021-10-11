#Models
from bookstoreApp.models import Employee, User

#Serializers
from .. import BaseProductSerializer, BaseProductListSerializer
from . import UserSerializer,UserUpdateSerializer

class EmployeeSerializer(BaseProductSerializer): 

    user= UserSerializer()
    class Meta:
        model= Employee
        fields = '__all__'
        list_serializer_class = BaseProductListSerializer
    
    def create(self, validated_data):        
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        return  Employee.objects.create(user_id= user_instance.id,**validated_data)
class EmployeeUpdateSerializer(EmployeeSerializer): 
    user= UserUpdateSerializer()