from django.db import models
from django.conf import settings 
from django.db.models import Q

user = settings.AUTH_USER_MODEL

class TaskManager(models.Manager):
    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        qs = super(TaskManager, self).get_queryset()
        return qs.filter(lookup)

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
    objects = TaskManager()

    def __str__(self):
        return self.title