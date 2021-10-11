#Models
from bookstoreApp.models import Sale

#Serializers
from bookstoreApp.serializers import SaleSerializer, SaleUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class SaleView(BaseIndependentView):
    
    custom_serializer = SaleSerializer
    update_serializer = SaleUpdateSerializer
    model = Sale
    

    