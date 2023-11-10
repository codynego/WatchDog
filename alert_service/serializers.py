from rest_framework import serializers
from .models import AlertRule
from data_manager.models import Server

class AlertRuleSerializer(serializers.ModelSerializer):
    server_id = serializers.CharField(write_only=True)
    class Meta:
        model = AlertRule
        fields = ['id', 'server', 'server_id', 'metric', 'threshold', 'condition', 'action']
        read_only_fields = ['server']

    def create(self, validated_data):
        server_id = validated_data.pop('server_id')
        server = Server.objects.get(pk=server_id)
        alert_rule = AlertRule.objects.create(server=server, **validated_data)
        return alert_rule
