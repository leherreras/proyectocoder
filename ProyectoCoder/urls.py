from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import login_request, register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('register/', register, name='Register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
