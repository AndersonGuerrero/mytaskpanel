from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True, help_text="Fecha de creacion")

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Usuario relacionado")
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, help_text="Proyecto relacionado")
    creation_date = models.DateTimeField(auto_now=True, help_text="Fecha de creacion")

    def __str__(self):
        return self.name