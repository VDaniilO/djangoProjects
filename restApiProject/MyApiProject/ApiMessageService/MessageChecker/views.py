from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Messages, Conditions
from .serializers import MessageSerializer


class MessageAPIList(generics.ListCreateAPIView):

     queryset = Messages.objects.all()
     serializer_class = MessageSerializer
     permission_classes = (IsAuthenticatedOrReadOnly, )

class MessageAPIUpdate(generics.RetrieveUpdateAPIView):

     queryset = Messages.objects.all()
     serializer_class = MessageSerializer
     permission_classes = (IsAuthenticated, )
#     authentication_classes = (TokenAuthentication,)


class MessageAPIDestroy(generics.RetrieveDestroyAPIView):

     queryset = Messages.objects.all()
     serializer_class = MessageSerializer
     permission_classes = (IsAdminOrReadOnly, )
