#Django
from django.http import Http404

#Django rest framework
from rest_framework.response import Response
from rest_framework import views, status

class BaseIndependentView(views.APIView):
    
    #Required variables
    custom_serializer = None
    update_serializer=None
    model = None
    
    #Get instance: returns the instance with the id indicated , otherwise it throws a 404 exception
    def get_instance(self, pk):
        try:
            return self.model.objects.filter(id=pk)
        except self.parent_model.DoesNotExist:
            raise Http404
    
    
    #List: returns a list with data of all filtered objects
    def get(self,request):
        instances= self.model.objects.all()
        instances_serializer = self.custom_serializer(instances, many=True)
        return Response(instances_serializer.data, status= status.HTTP_200_OK)
    
    #Create: creates objects based on supplied data  
    def post(self, request, *args, **kwargs):
        serializer = self.custom_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response({'message': 'successful creation'}, status= status.HTTP_201_CREATED)
    
    #Update: updates objects based on supplied data  
    def put(self, request, *args, **kwargs):
        instances_mapping= {
                            data['id'] : self.get_instance(data['id'])
                            for data in request.data
                            }
        serializer = self.update_serializer(instances_mapping, data=request.data, partial=True, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response({'message': 'successful update'}, status= status.HTTP_200_OK)
    
    #Delete: performs removal of required objects
    def delete(self, request, *args, **kwargs):
        for id in request.data:      
            instance= self.get_instance(id['id']).delete()
        return Response({'message': 'successful deletion'}, status= status.HTTP_204_NO_CONTENT)
    