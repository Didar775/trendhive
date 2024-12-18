from django.urls import path
from .views import GenerateOTPView, VerifyOTPView, otp_auth_view, RefreshTokenView

urlpatterns = [
    path('generate-otp/', GenerateOTPView.as_view(), name='generate_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('refresh/', RefreshTokenView.as_view(), name='verify_otp'),

    path('', otp_auth_view, name='otp_auth'),
]
