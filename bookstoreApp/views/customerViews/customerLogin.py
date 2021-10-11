#Django Rest framework
from rest_framework import status, views
from rest_framework.response import Response

#Simple JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomerLoginView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        tokenData = {
                        "username":request.data["username"],
                        "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_200_OK)