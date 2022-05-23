from rest_framework import serializers
from django.contrib.auth.models import User
from apiapp.models import todo

class TodoSerializer(serializers.ModelSerializer):
 
    userid = serializers.ReadOnlyField(source='owner.id')
  
    class Meta:
        model = todo
        fields = ['id', 'task', 'created_at', 'userid']

   
    
  
   

class UserSerializer(serializers.ModelSerializer):
    mess = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
 
    class Meta:
        model = User
        fields = ['id', 'username','mess']

