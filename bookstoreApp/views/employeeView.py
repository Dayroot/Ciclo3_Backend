#Base view
from .baseViews import ChildModelView
#Serializers
from bookstoreApp.serializers.employeeSerializer import EmployeeSerializer, EmployeeUpdateSerializer

  
class EmployeeView(ChildModelView):
    
    custom_serializer = EmployeeSerializer
    update_serializer = EmployeeUpdateSerializer
    
