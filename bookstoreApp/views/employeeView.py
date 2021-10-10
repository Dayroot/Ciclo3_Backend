#Base view
from .baseViews import BaseProductView
#Serializers
from bookstoreApp.serializers.employeeSerializer import EmployeeSerializer, EmployeeUpdateSerializer

  
class EmployeeView(BaseProductView):
    
    custom_serializer = EmployeeSerializer
    update_serializer = EmployeeUpdateSerializer
    
