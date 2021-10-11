#Models
from bookstoreApp.models import Reservation

#Serializers
from bookstoreApp.serializers import ReservationSerializer, ReservationUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView

class ReservationView(BaseIndependentView):
    
    custom_serializer = ReservationSerializer
    update_serializer = ReservationUpdateSerializer
    model = Reservation
    

    