from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, InviteUserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InviteUser(generics.CreateAPIView):
    serializer_class = InviteUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = InviteUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Invite sent successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)