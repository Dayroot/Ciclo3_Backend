from rest_framework.response import Response
from rest_framework.views import APIView
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.employeeSerializer import EmployeeSerializer

class EmployeeView(APIView):
    
    def get(self,request):
        employees= Employee.objects.all()
        employees_serializer =EmployeeSerializer(employees, many=True)
        return Response(employees_serializer.data)