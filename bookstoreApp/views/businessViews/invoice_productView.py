#Models
from bookstoreApp.models import Invoice_Product

#Serializers
from bookstoreApp.serializers import Invoice_ProductSerializer, Invoice_ProductUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class Invoice_ProductView(BaseIndependentView):
    custom_serializer = Invoice_ProductSerializer
    update_serializer = Invoice_ProductUpdateSerializer
    model = Invoice_Product
    