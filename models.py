from django.db import models
from decimal import Decimal
from CurrencyField import CurrencyField

# Create your models here.
class Quotation(models.Model):
    company = models.CharField(max_length=200)
    date_of_quote = models.DateTimeField('date quoted')
    total_price = CurrencyField(1.00)	

class Listings(models.Model):
    quotation = models.ForeignKey(Quotation)
    category = models.CharField(max_length=200)
    information = models.CharField(max_length=200)
    price = CurrencyField(1.00)
