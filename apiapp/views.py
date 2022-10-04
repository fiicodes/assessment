from django.shortcuts import render



from rest_framework import generics
from apiapp import serializers
from django.contrib.auth.models import User
from .models import todo
from rest_framework.permissions import *
from rest_framework.views import APIView

  
   
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView 

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
import jwt
    

#Authcontroller related function below



#class for jwt authentication and encoding the userdetails with tokens
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
     token=super().get_token(user)
     token['first name']=user.first_name
     token['last name']=user.last_name
     token['email']=user.email
     token['isactive']=user.is_active
     token['role']=user.is_superuser

     return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


#Todo API related functions below
#Todo API authentication using tokens

class CustomAuthTokenlogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username
           

        })
 

 #Here using djangomodelpermission we give user only the right to view the task in todoapi
#Django CRUD operation related classes
class TodoList(generics.ListCreateAPIView):
    permission_classes =  [DjangoModelPermissions]
   
    
   
    queryset = todo.objects.all()
    serializer_class = serializers.TodoSerializer
    

    def perform_create(self, serializer):

             serializer.save(owner=self.request.user)
         
#here giving adminuser to update,delete and retrive task from todo model
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    
    queryset = todo.objects.all()
    serializer_class = serializers.TodoSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

