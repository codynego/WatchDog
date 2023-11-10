from rest_framework import serializers
from .models import User
from data_manager.models import ServerManager
from data_manager.models import Server



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username']


class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerManager
        fields = ['id', 'user', 'server', 'permission']
        read_only_fields = ['user']

    
    def create(self, validated_data):
        server = Server.objects.get(pk=self.kwargs["pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        server_manager = ServerManager.objects.create(server=server, user=user, **validated_data)
        return 
    

