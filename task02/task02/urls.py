from django.contrib import admin
from django.urls import path  # Import the path function
from task02.admin import custom_admin_site  # Import your custom admin site

urlpatterns = [
    path('admin/', custom_admin_site.urls),  # Use the custom admin site
]
