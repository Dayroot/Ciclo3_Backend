#Django
from django.http import Http404

#Django rest framework
from django.views import generic
from rest_framework.response import Response
from rest_framework import views, status, generics, mixins, permissions

#Models
from bookstoreApp.models.workArea import WorkArea

#Serializers
from bookstoreApp.serializers.workAreaSerializer import WorkAreaSerializer

class WorkAreaView(generics.ListCreateAPIView):
    queryset = WorkArea.objects.all()
    serializer_class = WorkAreaSerializer
    

    