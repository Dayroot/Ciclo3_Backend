#Base view
from ..baseViews import ChildModelView
#Serializers
from bookstoreApp.serializers.productSerializers import BookSerializer, BookUpdateSerializer

  
class BookView(ChildModelView):
    
    custom_serializer = BookSerializer
    update_serializer = BookUpdateSerializer