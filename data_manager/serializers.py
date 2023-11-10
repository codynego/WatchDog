from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Server, Metric, AlertRule, Invite, ServerManager
from user_manager.models import User
from user_manager.serializers import UserSerializer
class ServerSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Server
        fields = ['id', 'hostname', 'ip_address', 'memory_capacity', 'cpu_capacity', 'disk_capacity', 'user']
        read_only_fields = ['user']


class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

    def create(self, validated_data):
        server = Server.objects.get(pk=self.kwargs["pk"])
        metric = Metric.objects.create(server=server, **validated_data)
        return metric


class AlertRuleSerializer(ModelSerializer):
    class Meta:
        model = AlertRule
        fields = '__all__'

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['id', 'server', 'email']
        read_only_fields = ['server']

    def create(self, validated_data):
        server = validated_data['server']
        email = validated_data['email']
        user = User.objects.filter(email=email).first()

        # If the user doesn't exist, create an invite
        if not user:
            invite = Invite.objects.create(server=server, email=email)
            return invite
        else:
            # If the user exists, check if they are already a server manager
            server_manager = ServerManager.objects.filter(server=server, user=user).first()
            if server_manager:
                raise serializers.ValidationError("User is already a server manager")
            else:
                # If the user exists but is not a server manager, create a server manager
                invite = Invite.objects.create(server=server, email=email)
                return invite
            