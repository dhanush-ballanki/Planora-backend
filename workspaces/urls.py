from django.urls import path
from .views import create_workspace

urlpatterns = [
    path('create/', create_workspace, name='create_workspace'),
]