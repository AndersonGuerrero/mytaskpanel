from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import  Project, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['name', 'start_date', 'delivery_date', 'tasks']


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ['name', 'description', 'start_date', 'delivery_date', 'user', 'project']

