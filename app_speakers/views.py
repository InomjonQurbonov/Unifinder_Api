from django.shortcuts import render
from app_speakers.models import Speakers
from app_speakers.serializers import SpeakersSerializer, GetSpeakersSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class SpeakersViewSet(ModelViewSet):
    queryset = Speakers.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return SpeakersSerializer
        return GetSpeakersSerializer