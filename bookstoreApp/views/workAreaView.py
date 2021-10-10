#Models
from bookstoreApp.models.workArea import WorkArea

#Serializers
from bookstoreApp.serializers.workAreaSerializer import WorkAreaSerializer, WorkAreaUpdateSerializer

#Base view
from .baseViews import BaseIndependentView
class WorkAreaView(BaseIndependentView):
    custom_serializer = WorkAreaSerializer
    update_serializer = WorkAreaUpdateSerializer
    model = WorkArea
    

    