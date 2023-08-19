from django.db import models
from django.conf import settings 

user = settings.AUTH_USER_MODEL

class Task(models.Model):
    status_choices = [
        ('NS', 'Not Started'),
        ('IP', 'In Progress'),
        ('C', 'Completed')
    ]

    owner = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=status_choices, default='NS')

    def __str__(self):
        return self.title