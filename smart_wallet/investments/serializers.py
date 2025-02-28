from rest_framework import serializers
from .models import Investments, InvestmentTypes, Dividends
from django.utils import timezone

class InvestmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = '__all__'

    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("The investment value cannot be negative or 0.")
        return value

    def validate_purchase(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("The purchase date cannot be later than the current date.")
        return value

    def validate_type(self, value):
        if not value.active:
            raise serializers.ValidationError("The selected investment type is not active.")
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
            raise serializers.ValidationError("The dividend value cannot be negative or 0.")
        return value

    def validate_receipt_date(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("The receipt date cannot be later than the current date.")
        return value

    def validate(self, data):
        investment = data.get('investment')
        receipt_date = data.get('receipt_date')
        user = data.get('user')

        errors = {}
        if investment and receipt_date:
            if receipt_date < investment.purchase:
                errors['receipt_date'] = "The dividend receipt date cannot be earlier than the investment purchase date."
        if investment and user:
            if user != investment.user:
                errors['user'] = "The dividend user must be the same as the associated investment's user."
        if errors:
            raise serializers.ValidationError(errors)
        return data