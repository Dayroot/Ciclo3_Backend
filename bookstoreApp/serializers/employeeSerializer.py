from rest_framework import serializers
from bookstoreApp.models.user import User
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.userSerializer import UserSerializer


# def employee_object(item):
#     print(item)  
#     userData = item.pop('user')
#     userInstance = User.objects.create_user(**userData)
#     employeeInstance= Employee(user= userInstance,**item)
#     employeeInstance.save()
#     return employeeInstance

# 
# class EmployeeListSerializer(serializers.ListSerializer): 
    
#     def create(self, validated_data): 
#         employees= list(map(employee_object,validated_data))                
#         #employees= [employee_object(item) for item in validated_data ]
#         return employees
# 

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
        #list_serializer_class = EmployeeListSerializer
        
    def create(self, validated_data):       
        userData = validated_data.pop('user')
        userInstance = User.objects.create_user(**userData)    
        employeeInstance= Employee.objects.create(user= userInstance,**validated_data)
        return employeeInstance
     
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
        