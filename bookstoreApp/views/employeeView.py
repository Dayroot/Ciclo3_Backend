from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from bookstoreApp.models.employee import Employee
from bookstoreApp.models.user import User
from bookstoreApp.serializers.employeeSerializer import EmployeeSerializer

class EmployeeDetailView(APIView):
    
    def get(self,request):
        employees= Employee.objects.all()
        employees_serializer =EmployeeSerializer(employees, many=True)
        return Response(employees_serializer.data)
    
class EmployeeCreateView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        message = {'result': 'successful creation'}
        return JsonResponse(message)
    
class EmployeeUpdateView(APIView):
    
    def post(self, request, *args, **kwargs):
        employee_list= [Employee.objects.get(user= employee['user'].pop('id')) for employee in request.data]
                        
        serializer = EmployeeSerializer(employee_list, data=request.data, partial=True, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        message = {'result': 'successful update'}
        
        return JsonResponse(message)