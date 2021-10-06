from django.db.models import fields
from rest_framework import serializers
from bookstoreApp.models.reservation import Reservation
from bookstoreApp.models.user import User
from bookstoreApp.models.product import Product

class ReservationListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data): 
        reservations=[]
        for item in validated_data:            
            reservations.append(Reservation(**item))   
        return Reservation.objects.bulk_create(reservations)
    
    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        reservation_mapping = {reservation.id: reservation for reservation in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for reservation_id, data in data_mapping.items():
            reservation = reservation_mapping.get(reservation_id, None)
            if reservation is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(reservation, data))

        # Perform deletions.
        for reservation_id, reservation in reservation_mapping.items():
            if reservation_id not in data_mapping:
                reservation.delete()
                
        return ret

    def to_representation(self, instance):
        reservation_representations= []
        for reservation in instance:
            reservation_representations.append({   
                'id': reservation.product_id,
                'quantity':reservation.quantity,
                'product_id':reservation.product_id,
                'user_id':reservation.user_id,
                }) 
        return reservation_representations

class ReservationSerializer(serializers.ModelSerializer):  
    class Meta:
        model= Reservation
        fields = '__all__'
        list_serializer_class = ReservationListSerializer
