from django.db import models

# Create your models here.
class Quotation(models.Model):
	company = models.CharField(max_length=200)
	date_of_quote = models.DateTimeField('date quoted')
	total_price - models.

	category = models.CharField(max_length=200)

class CurrencyField(models.DecimalField):
	__metaclass__ = models.SubfieldBase
	
	def to_python(self, value):
		try:
			return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
		except AttributerError:
			return None
