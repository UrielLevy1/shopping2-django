from django.contrib.auth import login, logout
from rest_framework import generics
from rest_framework import permissions
from rest_framework import views, status
from rest_framework.response import Response

from . import serializers


class LoginView(views.APIView):
   # This view should be accessible also for unauthenticated users.
   permission_classes = (permissions.AllowAny,)


   def post(self, request, format=None):
       serializer = serializers.LoginSerializer(data=self.request.data,
           context={ 'request': self.request })
       serializer.is_valid(raise_exception=True)
       user = serializer.validated_data['user']
       login(request, user)
       return Response(None, status=status.HTTP_202_ACCEPTED)
   
class LogoutView(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # Add sessionid to be returned from django - so we can read it from react:
        
    #     return Response({'session':request.session.session_key}, status=status.HTTP_202_ACCEPTED)   

class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user    

