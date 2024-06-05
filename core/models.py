from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
