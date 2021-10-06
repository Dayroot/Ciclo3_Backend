from rest_framework import serializers
from bookstoreApp.models.user import User
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.userSerializer import UserSerializer


class EmployeeListSerializer(serializers.ListSerializer):

    def create(self, validated_data): 
        employees=[]
        for item in validated_data:
            user_data = item.pop('user')
            user_instance = User.objects.create(**user_data)
            employees.append(Employee(user= user_instance,**item))   
        return Employee.objects.bulk_create(employees)

    def update(self, instance, validated_data):
        employee_mapping = {employee.user_id: employee for employee in instance}
        data_mapping = {item['user']['id']: item for item in validated_data}          
        ret = []                      
        for employee_id, data in data_mapping.items():          
            user_data = data.pop('user', None)         
            employee = employee_mapping.get(employee_id, None)                    
            if employee is None:               
                new_user= User.objects.create(**user_data)
                ret.append(self.child.create(user= new_user, **data))
            else:
                User.objects.filter(id=employee_id).update(**user_data)
                ret.append(self.child.update(employee, **data))
        
        for employee_id, employee in employee_mapping.items():
            if employee_id not in data_mapping:
                User.objects.get(id=employee_id).delete()
                #employee.delete()          
        return ret

    def to_representation(self, instance):
        employee_representations= []
        for employee in instance:
            employee_representations.append({   
                'id':employee.user_id,
                'username': employee.user.username,
                'fullname': employee.user.fullname,
                'datebirth': employee.user.datebirth,
                'email': employee.user.email,
                'identification': employee.user.identification,
                'phone number': employee.user.phone_number,
                'address': employee.user.address,
                'work area': employee.work_area.name,
                'salary': employee.salary,
                'is seller': employee.is_seller,
                'is inventory manager': employee.is_inventory_manager,
                'is admin': employee.is_admin
                }) 
        return employee_representations

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model= Employee
        fields = '__all__'
        list_serializer_class = EmployeeListSerializer

        