from django.contrib import admin
from app_conferency.models import Conferency, Sessions, ConferencyAgenda,ConferencySections, Partners, SubmissionFee

admin.site.register(Conferency)
admin.site.register(Sessions)
admin.site.register(ConferencySections)
admin.site.register(ConferencyAgenda)
admin.site.register(Partners)
admin.site.register(SubmissionFee)

