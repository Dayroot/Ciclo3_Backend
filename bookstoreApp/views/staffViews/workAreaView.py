#Models
from bookstoreApp.models import WorkArea

#Serializers
from bookstoreApp.serializers import WorkAreaSerializer, WorkAreaUpdateSerializer

#Base view
from ..baseViews import BaseIndependentView
class WorkAreaView(BaseIndependentView):
    
    custom_serializer = WorkAreaSerializer
    update_serializer = WorkAreaUpdateSerializer
    model = WorkArea
    

    