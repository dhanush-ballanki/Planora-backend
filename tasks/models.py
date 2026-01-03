from django.db import models
from users.models import User
from projects.models import Project

class Task(models.Model):
    STATUS = (
        ("TODO","TODO"),
        ("DOING","DOING"),
        ("DONE","DONE"),
    )

    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=10,choices=STATUS,default="TODO")
