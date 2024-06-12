from django.contrib import admin
from app_speakers.models import Speakers, SpeakerType, Organizations

admin.site.register(Speakers)

admin.site.register(SpeakerType)

admin.site.register(Organizations)