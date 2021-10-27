#Models
from bookstoreApp.models import User

#Serializers
from bookstoreApp.serializers import CustomerManagementSerializer, CustomerManagementUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class CustomerManagementView(BaseIndependentView):
    
    custom_serializer = CustomerManagementSerializer
    update_serializer = CustomerManagementUpdateSerializer
    model = User
    query_method = "filter"
    custom_filter = {"is_customer": True}