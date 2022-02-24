from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.users.views.viewSet import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]