from django.db import models
import uuid
from user_manager.models import User

# Create your models here.

class Server(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='servers')
    id = models.CharField(primary_key=True, max_length=200, editable=False)
    hostname = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    memory_capacity = models.IntegerField()
    cpu_capacity = models.IntegerField()
    disk_capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hostname} - {self.ip_address}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4().hex
        super(Server, self).save(*args, **kwargs)
    

class Metric(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    disk_usage = models.FloatField()
    network_throughput = models.FloatField()
    
    def __str__(self):
        return f"Metrics for {self.server.hostname} at {self.timestamp}"

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
