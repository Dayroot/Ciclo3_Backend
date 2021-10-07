from rest_framework.response import Response
from rest_framework.views import APIView
from bookstoreApp.models.employee import Employee
from bookstoreApp.serializers.employeeSerializer import EmployeeSerializer

class EmployeeDetailView(APIView):
    
    def get(self,request):
        employees= Employee.objects.all()
        employees_serializer =EmployeeSerializer(employees, many=True)
        return Response(employees_serializer.data)
    
class EmployeeCreateView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data, many=True) 
        return Response("correcto")