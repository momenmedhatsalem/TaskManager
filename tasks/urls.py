from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from rest_framework_simplejwt import views as jwt_views
# Initialize the router and register TaskViewSet with the 'tasks' URL
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# URL patterns for the API
urlpatterns = [
    path('', include(router.urls)),  # Include the API URLs for tasks
        # URL for obtaining JWT tokens (login)
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # URL for refreshing JWT tokens
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
