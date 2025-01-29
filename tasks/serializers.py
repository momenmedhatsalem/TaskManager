# tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Fields to be serialized (converted to JSON)
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'user']
