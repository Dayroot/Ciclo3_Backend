#Models
from bookstoreApp.models import Book

#Serializers
from ..baseSerializers import BaseProductSerializer, BaseProductListSerializer
from .productSerializer import ProductSerializer,ProductUpdateSerializer

class BookSerializer(BaseProductSerializer): 

    product= ProductSerializer()
    class Meta:
        model= Book
        fields = '__all__'
        list_serializer_class = BaseProductListSerializer
           
class BookUpdateSerializer(BookSerializer): 
    product= ProductUpdateSerializer()
    