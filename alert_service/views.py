from django.shortcuts import render
from rest_framework import generics
from .serializers import AlertRuleSerializer
from .models import AlertRule
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AlertAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AlertRule.objects.all()
    serializer_class = AlertRuleSerializer

    def get_queryset(self):
        return AlertRule.objects.filter(server__user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = AlertRuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Alert created successfully",
                "status": status.HTTP_201_CREATED,
                "alert": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
