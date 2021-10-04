from rest_framework import serializers
from bookstoreApp.models.user import User
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.userSerializer import UserSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = [
            'id', 
            'user', 
            'work_area', 
            'salary'
            ]
        
    def create(self, validated_data):
        
        userData = validated_data.pop('user')
        userInstance = User(**userData)
        userInstance.is_employee=True
        userInstance.save()
        
        employeeInstance= Employee.objects.create(user= userInstance,**validated_data)
        return employeeInstance
    
    def to_representation(self, obj):
        employee = Employee.objects.get(id= obj.id)
        user = User.objects.get(id=obj.user_id)
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
            'salary': employee.salary     
        }
        