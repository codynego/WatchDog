from django.db import models
from data_manager.models import Server


# Create your models here.
class AlertRule(models.Model):
    CONDITION_CHOICES = (
        ('greater_than', 'Greater Than'),
        ('less_than', 'Less Than'),
    )

    ACTION_CHOICES = (
        ('send_email', 'Send Email'),
        ('send_sms', 'Send SMS'),
    )
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    metric = models.CharField(max_length=255)
    threshold = models.FloatField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    action = models.CharField(max_length=255, choices=ACTION_CHOICES)

    def __str__(self):
        return f'Alert Rule for {self.metric} on {self.server.hostname}'