from django.db.models import fields
from rest_framework import serializers
from bookstoreApp.models import product
from bookstoreApp.models.product import Product
from bookstoreApp.models.magazine import Magazine
from bookstoreApp.serializers.productSerializer import ProductSerializer

class MagazineListSerializer(serializers.ListSerializer):

    def create(self, validated_data): 
        magazines=[]
        for item in validated_data:
            product_data = item.pop('product')
            product_instance = Product.objects.create(**product_data)
            magazines.append(Magazine(product= product_instance,**item))   
        return Magazine.objects.bulk_create(magazines)

    def update(self, instance, validated_data):
        magazine_mapping = {magazine.product_id: magazine for magazine in instance}
        data_mapping = {item['product']['id']: item for item in validated_data}          
        ret = []                      
        for magazine_id, data in data_mapping.items():          
            product_data = data.pop('product', None)         
            magazine = magazine_mapping.get(magazine_id, None)                    
            if magazine is None:               
                new_product= Product.objects.create(**product_data)
                ret.append(self.child.create(product= new_product, **data))
            else:
                Product.objects.filter(id=magazine_id).update(**product_data)
                ret.append(self.child.update(magazine, **data))
        
        for magazine_id, magazine in magazine_mapping.items():
            if magazine_id not in data_mapping:
                Product.objects.get(id=magazine_id).delete()
                #magazine.delete()          
        return ret

    def to_representation(self, instance):
        magazine_representations= []
        for magazine in instance:
            magazine_representations.append({   
                'id': magazine.product_id,
                'name':magazine.name,
                'edition':magazine.edition,
                'publication date':magazine.publication_date,
                'issn':magazine.issn,
                'editorial':magazine.editorial,
                'provider_name':magazine.product.provider_name,
                'stock':magazine.product.stock,
                'price':magazine.product.price
                }) 
        return magazine_representations

class MagazineSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 
    class Meta:
        model= Magazine
        fields = '__all__'
        list_serializer_class = MagazineListSerializer
