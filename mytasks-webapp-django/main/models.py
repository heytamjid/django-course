from django.db import models

# Create your models here.
    
class Tasksmodel (models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=100)
    isCompleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} : {self.description}"