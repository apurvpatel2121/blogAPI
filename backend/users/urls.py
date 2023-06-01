from django.urls import path
from users.views import *

urlpatterns = [
    path("",UserAPIView.as_view(),name="user_view"),
]