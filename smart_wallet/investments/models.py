from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class InvestmentTypes(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)     
    active = models.BooleanField(default=True)         

    def __str__(self):
        return self.name

class Investments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    name = models.CharField(max_length=100)
    type = models.ForeignKey(InvestmentTypes, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase = models.DateTimeField()                   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

class Dividends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dividends')
    investment = models.ForeignKey(Investments, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    receipt_date = models.DateTimeField()                   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Dividend {self.pk} - Investimento: {self.investment}"