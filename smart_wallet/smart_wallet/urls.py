from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Smart Wallet API",
      default_version='v1',
      description="API for investment management",
      contact=openapi.Contact(email="bergattoh@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/investments/', include('investments.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0
    ), name='schema-json'),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0
    ), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0
    ), name='schema-redoc'),
]