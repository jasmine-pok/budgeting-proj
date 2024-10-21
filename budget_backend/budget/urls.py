from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import register_user 

urlpatterns = [
    path('register/', register_user, name='register'),  # register endpoint to create new users
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # login endpoint for JWT toekn generation
    path('toekn/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # token refresh endpoint to get a new access token
]