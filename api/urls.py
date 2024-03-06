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
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),#Tested
    path('add-equipment/', AddEquipment.as_view(), name='add-equipment'),#Tested
    path('delete-equipment/<int:pk>/', DeleteEquipment.as_view(), name='delete-equipment'),#Tested
    path('list-unlist-equipment/<int:pk>/', ListUnlistEquipment.as_view(), name='list-unlist-equipment'),#Tested
    path('read-equipment/<int:pk>/', ReadEquipment.as_view(), name='read-equipment'),#Tested
    path('list-equipment/', ListEquipment.as_view(), name='list-equipment'),#Testedadd-equipment
    path('edit-equipment/<int:pk>/', EditEquipment.as_view(), name='edit-equipment'),#Tested
    path('list-basic-equipment/', ListBasicEquipment.as_view(), name='list-basic-equipment'),
    path('mark-attendance/', MarkAttendance.as_view(), name='mark-attendance'),
    path('delete-attendance/<int:attendance_id>/', DeleteAttendance.as_view(), name='delete-attendance'),
    path('enquiries-create/', EnquiryCreate.as_view(), name='enquiry-list'),
    path('enquiries/<int:pk>/', EnquiryRetrieve.as_view(), name='enquiry-retrieve'),
    path('enquiries/<int:pk>/update/', EnquiryUpdate.as_view(), name='enquiry-update'),
    path('enquiries/<int:pk>/delete/', EnquiryDelete.as_view(), name='enquiry-delete'),
    path('enquiries/', EnquiryListView.as_view(), name='enquiry-list'),
    path('create-gym-user/', GymUserCreateView.as_view(), name='create-gym-user'),
    path('register-gym-owner/', GymOwnerRegistrationView.as_view(), name='register_gym_owner'),
]
