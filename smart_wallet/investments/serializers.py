from rest_framework import serializers
from .models import Investments, InvestmentTypes, Dividends
from django.utils import timezone

class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = '__all__'

    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("The value of the investment cannot be negative or 0.")
        return value

    def validate_purchase(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("The purchase date cannot be later than the current date.")
        return value

class InvestmentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentTypes
        fields = '__all__'

class DividendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dividends
        fields = '__all__'

    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("The value of the investment cannot be negative or 0.")
        return value

    def validate_receipt_date(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("The receipt_date date cannot be later than the current date.")
        return value