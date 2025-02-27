# Import necessary modules and functions
from django.shortcuts import render                            
from rest_framework import status                                     # Status codes (200 OK, 400 Bad Request)
from rest_framework.response import Response                          # To send JSON responses
from rest_framework.decorators import api_view, permission_classes    # To create API views with function-based views
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User                           # Django's built-in User model for authentication
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

# Get the user model dynamically
User = get_user_model()

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
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        #validate the password using Django's built-in validators
        validate_password(password)

        # create the user with hased password
        user = User.objects.create_user(username=username, email=email, password=password)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Set JWT tokens in cookies
        response = Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        response.set_cookie(
            key='access_token', value=str(access_token), httponly=True, secure=True, samesite='None', path='/'
        )
        response.set_cookie(
            key='refresh_token', value=str(refresh), httponly=True, secure=True, samesite='None', path='/'
        )

        return response
    
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
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if fields are empty
        if not username or not password:
            return Response({'error' : 'All fields are required'}, 
                            status=status.HTTP_400_BAD_REQUEST
                            )

        # Authenticate user
        user = authenticate(request, username=username, password=password)
 
        if user is not None:           
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Set JWT tokens in cookies (with HttpOnly for security)
            response = Response({'message': 'User logged in successfully'}, 
                                status=status.HTTP_200_OK)
            
            response.set_cookie(
                key='access_token', value=str(access_token), httponly=True, secure=True, samesite='None', path='/'
            )
            response.set_cookie(
                key='refresh_token', value=str(refresh), httponly=True, secure=True, samesite='None', path='/'
            )

            return response

        else:
            return Response({'error' : 'Invalid credentials'}, 
                            status=status.HTTP_401_UNAUTHORIZED
                            )
    # GET requests:
    else:
        return Response({'error': 'Method not allowed.'}, 
                        status=status.HTTP_405_METHOD_NOT_ALLOWED
                        )
    
    

# User Logout
# @csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])      # Only logged-in users can log out
def user_logout(request):
    try:
        # Extract the refresh token from the cookies
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({"error": 'No refresh token found in cookies'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Blacklist the refresh token
        token = RefreshToken(refresh_token)
        token.blacklist()

        response = Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        logout(request)
        return response
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



