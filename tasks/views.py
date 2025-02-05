# tasks/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    # Retrieve tasks for the authenticated user only (filter by user)
    queryset = Task.objects.all()

    # Use the TaskSerializer to format data
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        """
        Optionally restricts the returned tasks to the authenticated user.
        """
        try:
            return Task.objects.filter(user=self.request.user)
        except:
            # Return that the user is not authorized
            return Task.objects.none()

    def perform_create(self, serializer):
        # Automatically associate the task with the authenticated user
        serializer.save(user=self.request.user)


class TaskView(TemplateView):
    template_name = "task_list.html"
    permission_classes = [IsAuthenticated]

class TaskFormView(TemplateView):
    template_name = "task_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.kwargs.get('task_id')
        context['task_id'] = task_id  # Pass task ID to the template
        context['is_editing'] = task_id is not None  # Check if editing
        return context
    

class LoginView(TemplateView):
    template_name = "login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SignupView(TemplateView):
    template_name = "signup.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context