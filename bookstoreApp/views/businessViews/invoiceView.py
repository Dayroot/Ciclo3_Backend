#Models
from bookstoreApp.models import Invoice

#Serializers
from bookstoreApp.serializers import InvoiceSerializer, InvoiceUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class InvoiceView(BaseIndependentView):
    
    custom_serializer = InvoiceSerializer
    update_serializer = InvoiceUpdateSerializer
    model = Invoice
    
