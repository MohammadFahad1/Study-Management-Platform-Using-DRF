from django.contrib import admin
from django.urls import path, include
from .views import root_view

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'), name='api-root'),
]
