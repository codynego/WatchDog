from django.db import models

# Create your models here.

class Server(models.Model):
    hostname = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    memory_capacity = models.IntegerField()
    cpu_capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hostname} - {self.ip_address}:{self.port}"
