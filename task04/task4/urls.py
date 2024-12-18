# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_and_convert, name='upload_and_convert'),
]
