from django.urls import path, include
from rest_framework import routers
from app_conferency.views import (
    ConferencyApiViewSet, SessionsApiViewSet,
    ConferencyAgendaApiViewSet, ConferencySectionApiViewSet, 
    PartnersApiViewSet, SubmissionFeeApiViewSet
    )

router = routers.DefaultRouter()

router.register(r'conferency', ConferencyApiViewSet)
router.register(r'sessions', SessionsApiViewSet)
router.register(r'agenda', ConferencyAgendaApiViewSet)
router.register(r'sections', ConferencySectionApiViewSet)
router.register(r'partners', PartnersApiViewSet)
router.register(r'Submission-fee', SubmissionFeeApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]