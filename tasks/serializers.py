from .models import * 
from rest_framework import serializers 
from datetime import date 
from .validators import *
from profiles.serializers import *

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[unique_title])
    due_date = serializers.DateField()
    owner = ProfileSerializer()
    class Meta:
        model = Task 
        fields = ['owner', 'pk', 'title', 'description', 'due_date', 'status']

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Cannot enter a date in the past")
        return value
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance