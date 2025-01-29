from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Initialize the router and register TaskViewSet with the 'tasks' URL
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# URL patterns for the API
urlpatterns = [
    path('api/', include(router.urls)),  # Include the API URLs for tasks
]
