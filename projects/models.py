from django.db import models
from workspaces.models import Workspace
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
