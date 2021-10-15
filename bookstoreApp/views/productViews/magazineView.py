#Base view
from bookstoreApp.views.baseViews import BaseProductView
from ..baseViews import BaseProductView
#Serializers
from bookstoreApp.serializers import MagazineSerializer, MagazineUpdateSerializer

  
class MagazineView(BaseProductView):
    query_method = "filter"
    custom_serializer = MagazineSerializer
    update_serializer = MagazineUpdateSerializer