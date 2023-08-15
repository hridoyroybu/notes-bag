from django.db import models

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
    rating = models.IntegerField(default=1)
    category = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    filterId = models.IntegerField(default=1)