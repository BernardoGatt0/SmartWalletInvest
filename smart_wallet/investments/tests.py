import pytest
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth import get_user_model
from .models import InvestmentTypes, Investments, Dividends
from .serializers import InvestmentsSerializer, DividendsSerializer

User = get_user_model()

# Fixtures for reusable objects

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def active_investment_type(db):
    return InvestmentTypes.objects.create(name='Stocks', active=True)

@pytest.fixture
def inactive_investment_type(db):
    return InvestmentTypes.objects.create(name='Bonds', active=False)

@pytest.fixture
def investment(db, user, active_investment_type):
    # Create an investment with a purchase date in the past
    return Investments.objects.create(
        user=user,
        name="Investment 1",
        type=active_investment_type,
        value=Decimal('1000.00'),
        purchase=timezone.now() - timezone.timedelta(days=10)
    )

# Tests for InvestmentsSerializer

def test_investments_serializer_valid(user, active_investment_type):
    data = {
        'user': user.id,
        'name': 'Test Investment',
        'type': active_investment_type.id,
        'value': '500.00',
        'purchase': (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer = InvestmentsSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

def test_investments_serializer_invalid_value(user, active_investment_type):
    data = {
        'user': user.id,
        'name': 'Test Investment',
        'type': active_investment_type.id,
        'value': '-100.00',
        'purchase': (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer = InvestmentsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'value' in serializer.errors

def test_investments_serializer_future_purchase(user, active_investment_type):
    data = {
        'user': user.id,
        'name': 'Test Investment',
        'type': active_investment_type.id,
        'value': '100.00',
        'purchase': (timezone.now() + timezone.timedelta(days=1)).isoformat()
    }
    serializer = InvestmentsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'purchase' in serializer.errors

def test_investments_serializer_inactive_investment_type(user, inactive_investment_type):
    data = {
        'user': user.id,
        'name': 'Test Investment',
        'type': inactive_investment_type.id,
        'value': '200.00',
        'purchase': (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer = InvestmentsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'type' in serializer.errors

# Tests for DividendsSerializer

def test_dividends_serializer_valid(user, investment):
    data = {
        'user': user.id,
        'investment': investment.id,
        'value': '50.00',
        'receipt_date': (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer = DividendsSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

def test_dividends_serializer_invalid_value(user, investment):
    data = {
        'user': user.id,
        'investment': investment.id,
        'value': '-50.00',
        'receipt_date': (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer = DividendsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'value' in serializer.errors

def test_dividends_serializer_receipt_date_before_purchase(user, investment):
    data = {
        'user': user.id,
        'investment': investment.id,
        'value': '50.00',
        # Set receipt_date to before the investment's purchase date
        'receipt_date': (investment.purchase - timezone.timedelta(days=1)).isoformat()
    }
    serializer = DividendsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'receipt_date' in serializer.errors

def test_dividends_serializer_wrong_user(db, user, active_investment_type):
    # Create a second user to simulate a mismatch
    other_user = User.objects.create_user(username='otheruser', password='password')
    investment = Investments.objects.create(
        user=user,
        name="Investment 2",
        type=active_investment_type,
        value=Decimal('1000.00'),
        purchase=timezone.now() - timezone.timedelta(days=10)
    )
    data = {
        'user': other_user.id,  # This user does not match the investment's user
        'investment': investment.id,
        'value': '100.00',
        'receipt_date': (timezone.now() - timezone.timedelta(days=1)).isoformat()
    }
    serializer = DividendsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'user' in serializer.errors