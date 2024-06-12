from django.urls import path, include
from rest_framework import routers

from app_speakers import views

router = routers.DefaultRouter()

router.register(r'speakers', views.SpeakersViewSet)

urlpatterns = [
    path('', include(router.urls))
]
