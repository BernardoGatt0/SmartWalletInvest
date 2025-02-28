from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import Investments, InvestmentTypes, Dividends
from .serializers import InvestmentsSerializer, InvestmentTypesSerializer, DividendsSerializer

class InvestmentTypesViewSet(viewsets.ModelViewSet):
    queryset = InvestmentTypes.objects.all()
    serializer_class = InvestmentTypesSerializer
    permission_classes = [IsAuthenticated]

class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer
    permission_classes = [IsAuthenticated]

class DividendsViewSet(viewsets.ModelViewSet):
    queryset = Dividends.objects.all()
    serializer_class = DividendsSerializer
    permission_classes = [IsAuthenticated]

class WalletInvestmentValueView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        total_investments = Investments.objects.filter(user_id=id).aggregate(total_value=Sum('value'))
        return Response(total_investments)


class WalletDividendValueView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        total_dividends = Dividends.objects.filter(user_id=id).aggregate(total_dividends=Sum('value'))
        return Response(total_dividends)