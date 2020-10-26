from django.urls import path, include
from .views import *

urlpatterns = [
    path('send/', sendEmail, name="send"),
]