from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255 ,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)