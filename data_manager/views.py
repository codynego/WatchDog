from django.shortcuts import render
from .models import Server, Metric, AlertRule
from rest_framework import generics
from .serializers import ServerSerializer, MetricSerializer, AlertRuleSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class DataCollector(generics.CreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def post(self, request, *args, **kwargs):
        server = Server.objects.get(pk=self.kwargs["pk"])
        serializer = MetricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(server=server)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class MetricList(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Metric.objects.objects.get(server_id=self.kwargs["pk"])
        return queryset
    
    def post(self, request, *args, **kwargs):
        server = Server.objects.get(pk=self.kwargs["pk"])
        serializer = MetricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(server=server)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
