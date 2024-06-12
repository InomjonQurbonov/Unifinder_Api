from rest_framework import serializers
from app_speakers.models import Speakers

class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = '__all__'

class GetSpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ['id', 'first_name', 'last_name', 'speaker_type']