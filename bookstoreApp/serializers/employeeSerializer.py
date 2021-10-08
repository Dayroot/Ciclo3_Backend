from rest_framework import serializers
from bookstoreApp.models.user import User
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.userSerializer import UserSerializer
from bookstoreApp.serializers.userSerializer import UserUpdateSerializer

class EmployeeUpdateListSerializer(serializers.ListSerializer):
    
    def update(self, employee_mapping, validated_data):

        data_mapping = {item['user']['id'] : item for item in validated_data}          
        ret = []                      
        for id, data in data_mapping.items():          
            user_data = data.pop('user', None)            
            employee = employee_mapping.get(id, None)                    
            User.objects.filter(id=id).update(**user_data)
            ret.append(employee.update(**data))                        
        return ret

class EmployeeListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data): 
        employees=[]
        for item in validated_data:
            user_data = item.pop('user')
            user_instance = User.objects.create(**user_data)
            employees.append(Employee(user= user_instance,**item))   
        return Employee.objects.bulk_create(employees)

    def to_representation(self, instance):
        
        employee_representations= []
        for employee in instance:
            employee_representations.append({ 
                'user': {
                    'id':employee.user_id,
                    'username': employee.user.username,
                    'fullname': employee.user.fullname,
                    'datebirth': employee.user.datebirth,
                    'gender':employee.user.gender,
                    'email': employee.user.email,
                    'identification': employee.user.identification,
                    'phone_number': employee.user.phone_number,
                    'address': employee.user.address    
                }, 
                'work_area': employee.work_area.name,
                'salary': employee.salary,
                'is_seller': employee.is_seller,
                'is_inventory_manager': employee.is_inventory_manager,
                'is_admin': employee.is_admin
                }) 
        return employee_representations

class EmployeeSerializer(serializers.ModelSerializer): 

    user= UserSerializer()

    class Meta:
        model= Employee
        fields = '__all__'
        list_serializer_class = EmployeeListSerializer

    def create(self, validated_data):        
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        return  Employee.objects.create(user_id= user_instance.id,**validated_data)
    
    
class EmployeeUpdateSerializer(serializers.ModelSerializer): 
    user= UserUpdateSerializer()
    class Meta:
        model= Employee
        fields = '__all__'
        list_serializer_class = EmployeeUpdateListSerializer


    