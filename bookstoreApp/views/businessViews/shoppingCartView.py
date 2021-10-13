#Models
from bookstoreApp.models import ShoppingCart

#Serializers
from bookstoreApp.serializers import ShoppingCartSerializer, ShoppingCartUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class ShoppingCartView(BaseIndependentView):
    
    custom_serializer = ShoppingCartSerializer
    update_serializer = ShoppingCartUpdateSerializer
    model = ShoppingCart
    

    