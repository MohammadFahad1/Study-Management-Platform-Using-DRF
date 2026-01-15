from django.contrib import admin
from django.urls import path, include
from .views import root_view
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Study Management Platform API",
      default_version='v1',
      description="The API documentation for the Study Management Platform.",
      terms_of_service="So many terms of services, you won't believe it.",
      contact=openapi.Contact(email="info@fahadbd.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'), name='api-root'),
] + debug_toolbar_urls()
