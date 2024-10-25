# Import necessary modules and functions
from django.shortcuts import render                                 
from rest_framework import status                                   # Status codes (200 OK, 400 Bad Request)
from rest_framework.response import Response                        # To send JSON responses
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token                   # To manage tokens if needed
from rest_framework.decorators import api_view, permission_classes                      # To create API views with function-based views
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User                         # Django's built-in User model for authentication
# from django.contrib.auth.hashers import make_password               # To hash passwords securely
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

# Register User API View
@csrf_exempt
@api_view(['POST']) # POST request handler for user registration
@permission_classes([AllowAny])
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
    
# User log in
@csrf_exempt
@api_view(['POST']) # POST request handler for user login
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if fields are empty
    if not username or not password:
        return Response({'error' : 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)       # either retrieve an existing token for user or create a new one if doesn't exist
        print(f"User {user.username} logged in with token: {token.key}")
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error' : 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])      # Only logged-in users can log out
def user_logout(request):
    try:
        token = Token.objects.get(user=request.user)        # Attempt to get token for the authenticated user
        token.delete()
        return Response({"detail" : "Successfully logged out."}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)

