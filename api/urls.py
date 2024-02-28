# urls.py

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#Tested
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#Tested
    path('send_otp/', SendOTP.as_view(), name='send_otp'),#Tested
    path('verify_otp/', VerifyOTP.as_view(), name='verify_otp'),#Tested
    path('add_user/', GymUserCreateAPIView.as_view(), name='add_user'),#Tested
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),#Tested
    path('users/block/<int:pk>/', UserBlockView.as_view(), name='user_block'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]
