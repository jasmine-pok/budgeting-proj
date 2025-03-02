"""
URL configuration for budgeting_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('budget/', include('budget.urls'))
]
"""

# debug views
@csrf_exempt  # Only for debugging - remove after troubleshooting
def debug_settings(request):
    if request.method == "GET" and request.GET.get('key') == 'debug123':  
        output = {
            'secret_key_hash': hash(settings.SECRET_KEY),
            'session_engine': getattr(settings, 'SESSION_ENGINE', 'Not set'),
            'session_cookie_name': getattr(settings, 'SESSION_COOKIE_NAME', 'Not set'),
            'session_cookie_secure': getattr(settings, 'SESSION_COOKIE_SECURE', 'Not set'),
            'csrf_cookie_secure': getattr(settings, 'CSRF_COOKIE_SECURE', 'Not set'),
            'allowed_hosts': getattr(settings, 'ALLOWED_HOSTS', []),
            'database_engine': settings.DATABASES['default']['ENGINE'],
        }
        return HttpResponse(str(output))
    return HttpResponse("Not authorized")

@csrf_exempt
def test_db(request):
    if request.method == "GET" and request.GET.get('key') == 'debug123':
        from django.contrib.auth.models import User
        try:
            count = User.objects.count()
            return HttpResponse(f"DB connection successful. User count: {count}")
        except Exception as e:
            return HttpResponse(f"DB error: {str(e)}")
    return HttpResponse("Not authorized")

@csrf_exempt
def test_session(request):
    if request.method == "GET" and request.GET.get('key') == 'debug123':
        request.session['test'] = 'working'
        if request.session.get('test') == 'working':
            return HttpResponse("Session writing works")
        else:
            return HttpResponse("Session writing failed")
    return HttpResponse("Not authorized")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('budget/', include('budget.urls'))
    # Add these at the end
    path('debug-settings/', debug_settings),
    path('test-db/', test_db),
    path('test-session/', test_session),
]