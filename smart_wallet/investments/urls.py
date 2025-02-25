from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentsViewSet, InvestmentTypesViewSet

router = DefaultRouter()
router.register(r'investments', InvestmentsViewSet)
router.register(r'investment-types', InvestmentTypesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]