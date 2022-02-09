from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import login_request, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('register/', register, name='Register'),
]
