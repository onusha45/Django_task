from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('get-subfolders/<int:id>/', get_subfolders, name="get_subfolders"),
]