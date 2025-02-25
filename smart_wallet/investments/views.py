from rest_framework import viewsets
from .models import Investments, InvestmentTypes
from .serializers import InvestmentsSerializer, InvestmentTypesSerializer
from rest_framework.permissions import IsAuthenticated

class InvestmentTypesViewSet(viewsets.ModelViewSet):
    queryset = InvestmentTypes.objects.all()
    serializer_class = InvestmentTypesSerializer
    permission_classes = [IsAuthenticated]

class InvestmentsViewSet(viewsets.ModelViewSet):
    queryset = Investments.objects.all()
    serializer_class = InvestmentsSerializer
    permission_classes = [IsAuthenticated]