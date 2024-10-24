# Import necessary modules and functions
from django.shortcuts import render                                 
from rest_framework import status                                   # Status codes (200 OK, 400 Bad Request)
from rest_framework.response import Response                        # To send JSON responses
from rest_framework.decorators import api_view                      # To create API views with function-based views
from django.contrib.auth.models import User                         # Django's built-in User model for authentication
from django.contrib.auth.hashers import make_password               # To hash passwords securely
from rest_framework_simplejwt.views import TokenObtainPairView      # JWT view to handle login
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext as _

# Register User API View
@api_view(['POST']) # POST request handler for user registration
def register_user(request):
    # Extract data from the request
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    # Check if any fields are empty
    if not username or not email or not password:
        return Response({'error' : 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        #validate the password using Django's built-in validators
        validate_password(password)

        # create the user with hased password
        user = User.objects.create_user(username=username, email=email, password=password)

        # send sucess response
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    
    except DjangoValidationError as e:
        return Response({'error': list(e.messages)}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        # catch any other errors
        return Response({'error': 'User registration failed. ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)