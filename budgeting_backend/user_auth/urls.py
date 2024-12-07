from django.urls import path
from .views import (
    register_user, 
    user_login, 
    user_logout
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView
)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),

    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # Obtains access and refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # Clients send a valid refresh token for a new access token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
    
]
