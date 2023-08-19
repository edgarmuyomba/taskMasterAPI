from .models import * 
from rest_framework import serializers 
from datetime import date 
from .validators import *

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[unique_title])
    due_date = serializers.DateField()
    class Meta:
        model = Task 
        fields = ['owner', 'pk', 'title', 'description', 'due_date', 'status']

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Cannot enter a date in the past")
        return value