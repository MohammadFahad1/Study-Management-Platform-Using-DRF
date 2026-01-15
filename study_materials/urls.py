from django.urls import path, include
from study_materials.views import ForgotPasswordView, VerifyOTPView, ResetPasswordView

urlpatterns = [
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify_otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset-password'),
]
