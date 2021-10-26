#Models
from bookstoreApp.models import ShoppingCart_Product

#Serializers
from bookstoreApp.serializers import ShoppingCart_ProductSerializer, ShoppingCart_ProductUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class ShoppingCart_ProductView(BaseIndependentView):

    custom_serializer = ShoppingCart_ProductSerializer
    update_serializer = ShoppingCart_ProductUpdateSerializer
    model = ShoppingCart_Product
    