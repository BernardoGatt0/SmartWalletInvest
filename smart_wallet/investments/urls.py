from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentsViewSet, InvestmentTypesViewSet, WalletValueList, DividendsViewSet

router = DefaultRouter()
router.register(r'investments', InvestmentsViewSet)
router.register(r'investment-types', InvestmentTypesViewSet)
router.register(r'dividends', DividendsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('wallet-value/<int:id>/user/', WalletValueList.as_view(), name='wallet-value'),
]