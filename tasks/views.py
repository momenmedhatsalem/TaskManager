# tasks/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    # Retrieve all tasks, but filter by the authenticated user
    queryset = Task.objects.all()
    # Use the TaskSerializer to format data
    serializer_class = TaskSerializer
    # Restrict access to authenticated users
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the task with the authenticated user
        serializer.save(user=self.request.user)
