from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from core.serializers import UserSerializer, ProjectSerializer, TaskSerializer
from core.models import  Project, Task


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint project.
    """
    queryset = Project.objects.all().order_by('-creation_date')
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint task.
    """
    queryset = Task.objects.all().order_by('-creation_date')
    serializer_class = TaskSerializer
