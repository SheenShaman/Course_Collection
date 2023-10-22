from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'courses', UserViewSet, basename='courses')

urlpatterns = [

] + router.urls
