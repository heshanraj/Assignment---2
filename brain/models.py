from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tasks')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.TextField()
    description = models.TextField(default = '')
    location = models.CharField(max_length=255,default = '')
    #organiser = models.CharField(max_length=100,default='')
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name