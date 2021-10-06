from rest_framework import serializers
from bookstoreApp.models.user import User
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.userSerializer import UserSerializer

"""
def employee_object(item):
    print(item)  
    userData = item.pop('user')
    userInstance = User.objects.create_user(**userData)
    employeeInstance= Employee(user= userInstance,**item) 
    return employeeInstance

class EmployeeListSerializer(serializers.ListSerializer): 
    

    def create(self, validated_data):                
        employees= [employee_object(item) for item in validated_data ]
        return Employee.objects.bulk_create(employees)
 
    def update(self, instance, validated_data):
        employee_mapping = {employee.id: employee for employee in instance}
        data_mapping = {item['user_id']: item for item in validated_data}
        ret = []
        
        for employee_id, data in data_mapping.items():
            employee = employee_mapping.get(employee_id, None)
            if employee is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(employee, data))
        
        for employee_id, employee in employee_mapping.items():
            if employee_id not in data_mapping:
                employee.delete()          
        return ret
""" 

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
        list_serializer_class = EmployeeListSerializer
        
    def create(self, validated_data):       
        userData = validated_data.pop('user')
        userInstance = User.objects.create_user(**userData)    
        return Employee.objects.create(user= userInstance,**validated_data)
        
     
    def to_representation(self, obj):
        employee = obj
        user = obj.user
        return {
            'id':user.id,
            'username': user.username,
            'fullname': user.fullname,
            'datebirth': user.datebirth,
            'email': user.email,
            'identification': user.identification,
            'phone number': user.phone_number,
            'address': user.address,
            'work area': employee.work_area.name,
            'salary': employee.salary,
            'is seller': employee.is_seller,
            'is inventory manager': employee.is_inventory_manager,
            'is admin': employee.is_admin
        }
        