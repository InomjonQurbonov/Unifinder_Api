from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from app_conferency.models import Conferency, Sessions, ConferencySections, ConferencyAgenda, Partners, SubmissionFee
from app_conferency.serializers import (
    ConferencySerializer,GetConferencySerializer, 
    SessionsSerializer, GetSessionsSerializer,
    ConferencyAgendaSerializer, GetConferencyAgendaSerializer,
    ConferencySectionSerializers, GetConferencySectionSerializer,
    PartnersSerializer, GetPartnersSerializer,
    SubmissionFeeSerializer, GetSubmissionFeeSerializer
    )


class ConferencyApiViewSet(ModelViewSet):
    queryset = Conferency.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ConferencySerializer
        return GetConferencySerializer
    

class SessionsApiViewSet(ModelViewSet):
    queryset = Sessions.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SessionsSerializer
        return GetSessionsSerializer
    

class ConferencyAgendaApiViewSet(ModelViewSet):
    queryset = ConferencyAgenda.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ConferencyAgendaSerializer
        return GetConferencyAgendaSerializer
    

class ConferencySectionApiViewSet(ModelViewSet):
    queryset = ConferencySections.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ConferencySectionSerializers
        return GetConferencySectionSerializer

class PartnersApiViewSet(ModelViewSet):
    queryset = Partners.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PartnersSerializer
        return GetPartnersSerializer

class SubmissionFeeApiViewSet(ModelViewSet):
    queryset = SubmissionFee.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubmissionFeeSerializer
        return GetSubmissionFeeSerializer