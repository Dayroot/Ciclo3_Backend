#Base view
from bookstoreApp.views.baseViews.baseProductView import BaseProductView
from ..baseViews import BaseProductView
#Serializers
from bookstoreApp.serializers.productSerializers import MagazineSerializer, MagazineUpdateSerializer

  
class MagazineView(BaseProductView):
    
    custom_serializer = MagazineSerializer
    update_serializer = MagazineUpdateSerializer