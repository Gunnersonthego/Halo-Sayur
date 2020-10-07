from django.urls import path, include
from rest_framework import routers
from rest_framework import urlpatterns
from .views import UserViewSet

#from .views import (
#    UserViewSet, SubmissionsViewSet, CustomAuthToken, UserProfileView
#)


router =routers.DefaultRouter()
router.register(r'',UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]