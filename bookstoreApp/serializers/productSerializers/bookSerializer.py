#Models
from bookstoreApp.models import Book

#Serializers
from ..baseSerializers import BaseProductSerializer, BaseProductUpdateSerializer, BaseProductListSerializer, BaseProductUpdateListSerializer
from .productSerializer import ProductSerializer,ProductUpdateSerializer

class BookSerializer(BaseProductSerializer): 

    product= ProductSerializer()
    class Meta:
        model= Book
        fields = '__all__'
        list_serializer_class = BaseProductListSerializer
           
class BookUpdateSerializer(BaseProductUpdateSerializer): 
    product= ProductUpdateSerializer()
    class Meta:
        model= Book
        fields = '__all__'
        list_serializer_class = BaseProductUpdateListSerializer