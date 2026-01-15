from django.urls import path, include
from study_materials.views import ForgotPasswordView

urlpatterns = [
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
]
