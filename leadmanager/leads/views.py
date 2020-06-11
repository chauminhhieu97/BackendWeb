# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Manh
from .models import User
from rest_framework import viewsets, generics, mixins, views, filters
from rest_framework import permissions
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


from rest_framework import status
# Register API

# AllowAny = IsAuthuen


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() == False:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print("before save user")
        user = serializer.save()
        print("save user")
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


# Login APIp
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })

# Get User API
