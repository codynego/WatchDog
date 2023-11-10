from django.contrib import admin
from .models import Metric, Server

# Register your models here.
admin.site.register(Metric)
admin.site.register(Server)

