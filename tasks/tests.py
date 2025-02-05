from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task  # Ensure you have a Task model imported

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        
        # Create some test tasks
        self.task1 = Task.objects.create(title='Task 1', description='First Task', user=self.user)
        self.task2 = Task.objects.create(title='Task 2', description='Second Task', user=self.user)
        
        self.url = '/api/tasks/'  # Ensure this matches your router's registered URL

    def test_get_list_of_tasks(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Task 1')
        self.assertEqual(response.data[1]['title'], 'Task 2')
