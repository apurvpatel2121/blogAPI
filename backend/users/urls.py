from django.urls import path
from users.views import *
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("",UserAPIView.as_view(),name="user_view"),
    path('login/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]