from django.urls import path, include
from rest_framework import routers
from app_users.views import UserApiViewSet, password_change_view, password_reset_view

router = routers.DefaultRouter()

router.register(r'users', UserApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('password-change/', password_change_view, name='password-change'),
    path('password-reset/', password_reset_view, name='password-reset'),
]