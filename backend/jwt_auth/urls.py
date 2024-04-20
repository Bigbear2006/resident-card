from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from . import views

urlpatterns = [
    path('get-token/', token_obtain_pair),
    path('refresh-token/', token_refresh),
    path('register-user/', views.RegisterUserAPIView.as_view()),
    path('user-info/', views.UserInfoAPIView.as_view()),
    path('update-user/', views.UpdateUserAPIView.as_view()),
]
