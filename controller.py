from RenovationPlanner.models import Quotation,Listings
import sys
from django.utils import timezone

class controller :
   def listAllCompanies(self):
      	return Quotation.objects.all() 

   def addNewCompany(self, name):
        try :
	    quotation = Quotation(company=name,
				date_of_quote=timezone.now(),
				total_price=1999.00)
            quotation.save()
            return True
        except :
            print "Error:", sys.exc_info()[0]
            return False
