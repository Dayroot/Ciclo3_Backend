from rest_framework import serializers
from bookstoreApp.models.user import User
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.userSerializer import UserSerializer

# class EmployeeListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
        


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
        
    def create(self, validated_data):
        
        userData = validated_data.pop('user')
        userInstance = User(**userData)
        userInstance.save()
        
        employeeInstance= Employee.objects.create(user= userInstance,**validated_data)
        return employeeInstance
    
    def to_representation(self, obj):
        employee = obj
        user = obj.user
        return {
            'id':employee.id,
            'username': user.username,
            'fullname': user.fullname,
            'datebirth': user.datebirth,
            'email': user.email,
            'identification': user.identification,
            'phone number': user.phone_number,
            'address': user.address,
            'work area': employee.work_area,
            'salary': employee.salary,
            'is seller': employee.is_seller,
            'is inventory manager': employee.is_inventory_manager,
            'is admin': employee.is_admin
        }
        