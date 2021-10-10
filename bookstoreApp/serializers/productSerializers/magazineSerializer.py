#Models
from bookstoreApp.models import Magazine

#Serializers
from ..baseSerializers import BaseProductSerializer,  BaseProductListSerializer
from .productSerializer import ProductSerializer,ProductUpdateSerializer

class MagazineSerializer(BaseProductSerializer): 

    product= ProductSerializer()
    class Meta:
        model= Magazine
        fields = '__all__'
        list_serializer_class = BaseProductListSerializer
           
class MagazineUpdateSerializer(MagazineSerializer): 
    product= ProductUpdateSerializer()
