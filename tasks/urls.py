from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskView, TaskFormView, SignupView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.views.generic.base import RedirectView

# Initialize the router and register TaskViewSet with the 'tasks' URL
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# URL patterns for the API
urlpatterns = [
    path('api/', include(router.urls)),  # Include the API URLs for tasks
    # URL for obtaining JWT tokens (login)
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path('', RedirectView.as_view(url='/tasks/', permanent=False)),  # Redirect root to /tasks
    
    # register / auth
    path('api/user/register/', include('dj_rest_auth.registration.urls')),
    # Task list template
    path("tasks/", TaskView.as_view(), name="tasks"),

    # Task form template
    path("tasks/form/", TaskFormView.as_view(), name="task_create"),  # Create a new task
    path("tasks/form/<int:task_id>/", TaskFormView.as_view(), name="task_edit"),

    # Signup template
    path("signup/", SignupView.as_view(), name="signup"),

    # Login template
    path("login/", LoginView.as_view(), name="login"),

]
