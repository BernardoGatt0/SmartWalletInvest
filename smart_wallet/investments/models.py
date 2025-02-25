from django.db import models

class InvestmentTypes(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)     
    active = models.BooleanField(default=True)         

    def __str__(self):
        return self.name

class Investments(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(InvestmentTypes, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase = models.DateTimeField()                   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
