from django.db import models
from users.models import User
# Create your models here.

class Workspace(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class WorkspaceMember(models.Model):
    ROLE_CHOICES = (
    ('ADMIN', 'ADMIN'),
    ('MEMBER', 'MEMBER'),
    ('VIEWER', 'VIEWER'),
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)