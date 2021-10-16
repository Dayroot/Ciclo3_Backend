#Base view
from ..baseViews import BaseProductView
#Serializers
from bookstoreApp.serializers import BookSerializer, BookUpdateSerializer

  
class BookView(BaseProductView):
    
    custom_serializer = BookSerializer
    update_serializer = BookUpdateSerializer