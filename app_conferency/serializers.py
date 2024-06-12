from rest_framework import serializers
from app_conferency.models import Conferency, Sessions, ConferencySections, ConferencyAgenda, Partners, SubmissionFee


class ConferencySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Conferency
        fields = '__all__'
        
        
        
class GetConferencySerializer(serializers.Serializer):
    
    
    class Meta:
        model = Conferency
        fields = ['id', 'conf_theme', 'conf_title', 'conf_date']
        

class SessionsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Sessions
        fields = '__all__'
        
        
class GetSessionsSerializer(serializers.Serializer):
    
    
    class Meta:
        model = Sessions
        fields = ['id', 'conferency', 'session_title', 'session_speaker']
        

class ConferencySectionSerializers(serializers.Serializer):
    
    
    class Meta:
        model = ConferencySections
        fields = '__all__'
        

class GetConferencySectionSerializer(serializers.Serializer):
    
    
    class Meta:
        model = ConferencySections
        fields = ['id', 'conferency', 'section_title']


class ConferencyAgendaSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ConferencyAgenda
        fields = '__all__'
        

class GetConferencyAgendaSerializer(serializers.Serializer):
    
    
    class Meta:
        model = ConferencyAgenda
        fields = ['id', 'conferency', 'agenda_title'] 


class PartnersSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Partners
        fields = '__all__'
        

class GetPartnersSerializer(serializers.Serializer):
    
    
    class Meta:
        model = Partners
        fields = ['id', 'conferency', 'partner_name', 'partner_logo']
        

class SubmissionFeeSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = SubmissionFee
        fields = "__all__"
        

class GetSubmissionFeeSerializer(serializers.Serializer):
    
    
    class Meta:
        model = SubmissionFee
        fields = ['id', 'conferency', 'sub_title', 'sub_price']