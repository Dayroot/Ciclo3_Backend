from rest_framework import serializers
from bookstoreApp.models import ShoppingCart_Product
from ..baseSerializers import BaseIndepentSerializer, BaseIndepentListSerializer

class ShoppingCart_ProductSerializer(BaseIndepentSerializer): 
    
    class Meta:
        model= ShoppingCart_Product
        fields = '__all__'
        list_serializer_class = BaseIndepentListSerializer
    
    def to_representation(self, instance):
        if (instance.product.type == "book"):  
            return {
                    "title": instance.product.Books.title,
                    "author": instance.product.Books.author,
                    "isbn": instance.product.Books.isbn,
                    "type": instance.product.type,
                    "Quantity": instance.quantity,
                    "Price by unit": instance.product.price,
                    "Total": instance.quantity * instance.product.price, 
            }
        elif (instance.product.type == "magazine"):  
            return {
                    "name": instance.product.Magazines.name,
                    "author": instance.product.Magazines.author,
                    "issn": instance.product.Magazines.issn,
                    "type": instance.product.type,
                    "Quantity": instance.quantity,
                    "Price by unit": instance.product.price,
                    "Total": instance.quantity * instance.product.price,
            }

class ShoppingCart_ProductUpdateSerializer(ShoppingCart_ProductSerializer):
    id = serializers.IntegerField()
    