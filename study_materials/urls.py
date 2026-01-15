from django.urls import path, include
from study_materials.views import ForgotPasswordView, VerifyOTPView

urlpatterns = [
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify_otp/', VerifyOTPView.as_view(), name='verify-otp'),
]
