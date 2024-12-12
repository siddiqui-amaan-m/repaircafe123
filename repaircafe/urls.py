from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('users.urls')),  # Add this line to include user app's API routes
]

urlpatterns += staticfiles_urlpatterns()