from django.urls import path
from .views import register_user, user_login
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='user_login'),
    
]
