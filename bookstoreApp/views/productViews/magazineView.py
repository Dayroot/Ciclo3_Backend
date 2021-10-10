#Base view
from ..baseViews import ChildModelView
#Serializers
from bookstoreApp.serializers.productSerializers import MagazineSerializer, MagazineUpdateSerializer

  
class MagazineView(ChildModelView):
    
    custom_serializer = MagazineSerializer
    update_serializer = MagazineUpdateSerializer