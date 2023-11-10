from django.db import models
import uuid
from user_manager.models import User
from django.utils import timezone

# Create your models here.

class Server(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='servers', null=True)
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



        return f"{self.user.username} - {self.hostname}"


   

class Metric(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    disk_usage = models.FloatField()
    network_throughput = models.FloatField()
    
    def __str__(self):
        return f"Metrics for {self.server.hostname} at {self.timestamp}"


    

class Invite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"Invite for {self.email} to join {self.server}"

    def mark_as_used(self):
        self.used = True
        self.save()

class ServerManager(models.Model):
    PERMISSION_CHOICES = (
        ('read', 'Read'),
        ('write', 'Write'),
        ('admin', 'Admin'),
    )
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.CharField(max_length=200, choices=PERMISSION_CHOICES, default='read')

    def __str__(self):
        return f"{self.user.username} - {self.server.hostname}"
