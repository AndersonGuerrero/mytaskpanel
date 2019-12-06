from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer, ProjectSerializer, TaskSerializer
from api.models import  Project, Task


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint users.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint project.
    """
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all().order_by('-creation_date')
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint task.
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-creation_date')
    serializer_class = TaskSerializer

    @action(
        methods=['get'],
        detail=False,
        permission_classes=[IsAuthenticated],
        name='Find tasks by project and user id',
        description='set parameter user and project for GET'
    )
    def by_project(self,request):
        """ API endpoint task by project.\n
            set parameter user and project for GET
        """
        project_id = request.GET.get('project')
        user_id = request.GET.get('user')
        user = self.request.user
        queryset = Task.objects.filter(
            project_id=project_id,
            user_id=user_id
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
