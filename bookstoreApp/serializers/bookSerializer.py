from django.db.models import fields
from rest_framework import serializers
from bookstoreApp.models import product
from bookstoreApp.models.product import Product
from bookstoreApp.models.book import Book
from bookstoreApp.serializers.productSerializer import ProductSerializer

class BookListSerializer(serializers.ListSerializer):

    def create(self, validated_data): 
        books=[]
        for item in validated_data:
            product_data = item.pop('product')
            product_instance = Product.objects.create(**product_data)
            books.append(Book(product= product_instance,**item))   
        return Book.objects.bulk_create(books)

    def update(self, instance, validated_data):
        book_mapping = {book.product_id: book for book in instance}
        data_mapping = {item['product']['id']: item for item in validated_data}          
        ret = []                      
        for book_id, data in data_mapping.items():          
            product_data = data.pop('product', None)         
            book = book_mapping.get(book_id, None)                    
            if book is None:               
                new_product= Product.objects.create(**product_data)
                ret.append(self.child.create(product= new_product, **data))
            else:
                Product.objects.filter(id=book_id).update(**product_data)
                ret.append(self.child.update(book, **data))
        
        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                Product.objects.get(id=book_id).delete()
                #book.delete()          
        return ret

    def to_representation(self, instance):
        book_representations= []
        for book in instance:
            book_representations.append({   
                'id': book.product_id,
                'title':book.title,
                'author':book.author,
                'publication date':book.publication_date,
                'isbn':book.isbn,
                'editorial':book.editorial,
                'provider_name':book.product.provider_name,
                'stock':book.product.stock,
                'price':book.product.price
                }) 
        return book_representations

class BookSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 
    class Meta:
        model= Book
        fields = '__all__'
        list_serializer_class = BookListSerializer
        
    
    