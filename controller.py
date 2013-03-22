from RenovationPlanner.models import Quotation,Listings
import sys
from django.utils import timezone

class controller :
   def listAllCompanies(self):
      	return Quotation.objects.all() 

   def addNewCompany(self, name, date, price):
        try :
	    quotation = Quotation(company=name,
				date_of_quote=date,
				total_price=price)
            quotation.save()
            return True
        except :
            print "Error:", sys.exc_info()[0]
            return False
