from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentsViewSet, InvestmentTypesViewSet, DividendsViewSet, WalletInvestmentValueView, WalletDividendValueView

router = DefaultRouter()
router.register(r'investments', InvestmentsViewSet)
router.register(r'investment-types', InvestmentTypesViewSet)
router.register(r'dividends', DividendsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('wallets/investment/<int:id>/user/', WalletInvestmentValueView.as_view(), name='wallet_investment_value'),
    path('wallets/dividends/<int:id>/user/', WalletDividendValueView.as_view(), name='wallet_dividend_value'),
]