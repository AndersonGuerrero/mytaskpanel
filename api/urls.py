from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]