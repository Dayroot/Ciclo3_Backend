#Django
from django.http import Http404

#Django rest framework
from rest_framework.response import Response
from rest_framework import views, status

class BaseProductView(views.APIView):
    
    #Required variables
    custom_serializer = None
    update_serializer = None
    
    
    #optional variables
    
    # Method that will be used to obtain the instances from which the data will be returned. It can take the value of all or filter, by default it will be all.
    query_method = "all"
    
    #Internal variables
    model = None
    parent_model= None
    parent_model_name= None
    defined_variables =False
    
    def define_variables(self):
        if (self.defined_variables is False and self.custom_serializer is not None and self.update_serializer is not None):
            self.model = self.custom_serializer.Meta.model
            self.parent_model= self.model.PARENT_MODEL
            self.parent_model_name= self.model.PARENT_MODEL_NAME
            self.defined_variables = True
        
    #List: returns a list with data of all filtered objects
    def get(self,request):
        self.define_variables()
        if self.query_method is "all" :
            instances= self.model.objects.all()
            
        elif self.query_method is "filter":
            instances= self.model.objects.filter(**request.data)
            
        instances_serializer = self.custom_serializer(instances, many=True)
        return Response(instances_serializer.data, status= status.HTTP_200_OK)
    
    #Create: creates objects based on supplied data  
    def post(self, request, *args, **kwargs):
        self.define_variables()
        serializer = self.custom_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response({'message': 'successful creation'}, status= status.HTTP_201_CREATED)
    
    #Update: updates objects based on supplied data  
    def put(self, request, *args, **kwargs):  
        self.define_variables()
        instances_mapping= {
                            data[self.parent_model_name]['id'] : 
                                self.model.objects.filter( **{self.parent_model_name:data[self.parent_model_name]['id']})
                            for data in request.data
                            }
        serializer = self.update_serializer(instances_mapping, data=request.data, partial=True, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response({'message': 'successful update'}, status= status.HTTP_200_OK)
    
    #Get user: returns the instance with the id indicated , otherwise it throws a 404 exception
    def get_parent_instance(self, pk):
        try:
            return self.parent_model.objects.get(id=pk)
        except self.parent_model.DoesNotExist:
            raise Http404
    
    #Delete: performs removal of required objects
    def delete(self, request, *args, **kwargs):
        self.define_variables()
        for id in request.data:      
            parent_instance= self.get_parent_instance(id['id']).delete()
        return Response({'message': 'successful deletion'}, status= status.HTTP_200_OK)
    
    