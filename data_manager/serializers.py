from rest_framework.serializers import ModelSerializer
from .models import Server, Metric, AlertRule

class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


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