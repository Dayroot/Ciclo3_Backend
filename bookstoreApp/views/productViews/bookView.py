#Base view
from ..baseViews import BaseProductView
#Serializers
from bookstoreApp.serializers import BookSerializer, BookUpdateSerializer

  
class BookView(BaseProductView):
    
    query_method = "filter"
    custom_serializer = BookSerializer
    update_serializer = BookUpdateSerializer