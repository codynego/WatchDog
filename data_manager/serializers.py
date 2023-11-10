from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Server, Metric, Invite, ServerManager
from user_manager.models import User
from user_manager.serializers import UserSerializer


class ServerSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Server
        fields = ['id', 'hostname', 'ip_address', 'memory_capacity', 'cpu_capacity', 'disk_capacity', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        server = Server.objects.create(user=user, **validated_data)
        return server


class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

    def create(self, validated_data):
        server = Server.objects.get(pk=self.kwargs["pk"])
        metric = Metric.objects.create(server=server, **validated_data)
        return metric



class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['id', 'server', 'email']
        read_only_fields = ['server']

    def create(self, validated_data):
        server = validated_data['server']
        email = validated_data['email']
        user = User.objects.filter(email=email).first()

        server_manager = ServerManager.objects.filter(server=server, user=user).first()
        if server_manager:
            raise serializers.ValidationError("User is already a server manager")
        else:
            invite = Invite.objects.create(server=server, email=email)
            return invite