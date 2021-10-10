#Models
from bookstoreApp.models import Magazine

#Serializers
from ..baseSerializers import BaseProductSerializer, BaseProductUpdateSerializer, BaseProductListSerializer, BaseProductUpdateListSerializer
from .productSerializer import ProductSerializer,ProductUpdateSerializer

class MagazineSerializer(BaseProductSerializer): 

    product= ProductSerializer()
    class Meta:
        model= Magazine
        fields = '__all__'
        list_serializer_class = BaseProductListSerializer
           
class MagazineUpdateSerializer(BaseProductUpdateSerializer): 
    product= ProductUpdateSerializer()
    class Meta:
        model= Magazine
        fields = '__all__'
        list_serializer_class = BaseProductUpdateListSerializer
