from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegistrationTests(APITestCase):

    def test_successful_registration(self):
        """Test registering a new user with valid data."""
        data = {
            "username": "testuser",
            "password": "StrongPassword123",
            "email": "testuser@example.com"
        }
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("message", response.data)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_registration_with_missing_fields(self):
        """Test registering a user with missing required fields."""
        data = {"username": "testuser"}  # Missing password and email
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_registration_with_weak_password(self):
        """Test registering a user with a weak password."""
        data = {
            "username": "testuser",
            "password": "123",
            "email": "testuser@example.com"
        }
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_registration_with_duplicate_username(self):
        """Test registering a user with an existing username."""
        User.objects.create_user(username="testuser", password="StrongPassword123")
        data = {
            "username": "testuser",
            "password": "AnotherPassword123",
            "email": "testuser2@example.com"
        }
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

class UserAuthTests(APITestCase):
    """"
    Tests for user authentication endpoints.
    """

    def setUp(self):
        """
        Create a test user and set the login endpoint.
        """
        self.user = User.objects.create_user(username='exampleuser', 
                                             password='password123')
        self.login_url = '/auth/login/'

    def test_successful_login(self):
        """
        Ensure user can log in with valid credentials
        """
        data = {'username': 'exampleuser', 
                'password': 'password123'
                }
        response = self.client.post(self.login_url, data)

        # check if the resonse status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verify tokens are returned in cookies
        self.assertIn('access_token', response.cookies)
        self.assertIn('refresh_token', response.cookies)
        
    def test_login_with_invalid_credentials(self):
        """
        Ensure login fails with invalid credentials
        """
        data = {'username': 'wrongusername',
                'password': 'wrongpassword'
                }
        response = self.client.post(self.login_url, data)

        # Check for 401 unathorized status
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Verify error message is returned
        self.assertIn('error', response.data)

    def test_login_with_missing_fields(self):
        """
        Ensure login fails when required fields are missing.
        """
        data = {'username': 'exampleuser'}  # Password missing
        response = self.client.post(self.login_url, data)
        
        # Check for 400 BAD REQUEST status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Verify error message
        self.assertEqual(response.data['error'], 'All fields are required')

    def test_inactive_user_login(self):
        """
        Ensure inactive users cannot log in.
        """
        # Deactivate the user
        self.user.is_active = False
        self.user.save()
        
        data = {'username': 'exampleuser', 
                'password': 'password123'}
        response = self.client.post(self.login_url, data)
        
        # Check for 401 UNAUTHORIZED status
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_get_request(self):
        """
        Ensure login fails if a GET request is sent instead of POST.
        """
        response = self.client.get(self.login_url)
        
        # Check for 405 METHOD NOT ALLOWED status
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_tokens_are_http_only(self):
        """
        Ensure the tokens are set in cookies with HttpOnly for security.
        """
        data = {'username': 'exampleuser', 
                'password': 'password123'}
        response = self.client.post(self.login_url, data)
        
        # Check if cookies have HttpOnly flag
        access_token_cookie = response.cookies.get('access_token')
        refresh_token_cookie = response.cookies.get('refresh_token')
        
        self.assertTrue(access_token_cookie['httponly'])
        self.assertTrue(refresh_token_cookie['httponly'])

class UserLogoutTests(APITestCase):

    def setUp(self):
        """Set up a user and log them in to obtain tokens."""
        self.user = User.objects.create_user(username="exampleuser", 
                                             password="StrongPassword123")
        response = self.client.post('/auth/login/', {"username": "exampleuser", 
                                                     "password": "StrongPassword123"})
        self.access_token = response.cookies.get('access_token').value
        self.refresh_token = response.cookies.get('refresh_token').value
        
        # Use the access token for Authorization header
        self.token = f'Bearer {self.access_token}'

    def test_successful_logout(self):
        """Test logging out a user with valid tokens."""
        self.client.cookies['refresh_token'] = self.refresh_token
        response = self.client.post('/auth/logout/', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)

    def test_logout_without_token(self):
        """Test logging out without providing tokens."""
        response = self.client.post('/auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)

    def test_logout_with_invalid_token(self):
        """Test logging out with an invalid or expired token."""
        self.client.cookies['refresh_token'] = "invalid_token"
        response = self.client.post('/auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)

