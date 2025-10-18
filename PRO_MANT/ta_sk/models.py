import uuid

from django.db import models

from account.models import User
from project.models import Project
from todolist.models import Task


class ta_sk(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='ta_sk', on_delete=models.CASCADE)
    todolist = models.ForeignKey(Task, related_name='ta_sk', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='ta_sk', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
