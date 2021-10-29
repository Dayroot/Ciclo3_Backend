#Django
from django.conf import settings
from django.contrib.auth.hashers import make_password
#Django Rest framework
from rest_framework import views, status
from rest_framework.response import Response

#Simple JWT
from rest_framework_simplejwt.backends import TokenBackend

#model
from bookstoreApp.models import User


class UserUpdateView(views.APIView):
     
    def put(self, request, *args, **kwargs):
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        if data.get("password") != None:
            some_salt= 'mMUj0DrIK6vgtdIYepkIxN'
            data['password'] = make_password(data['password'], some_salt)
            
        instance = User.objects.filter(id= kwargs['pk'])
        instance.update(**data)
        return Response({'message': 'successful update'}, status= status.HTTP_200_OK)
    