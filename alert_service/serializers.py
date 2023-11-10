from rest_framework.serializers import ModelSerializer
from .models import AlertRule

class AlertRuleSerializer(ModelSerializer):
    class Meta:
        model = AlertRule
        fields = '__all__'