"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from RenovationPlanner.controller import controller
from django.utils.timezone import datetime 

class controllerTest(TestCase):
    def test_addNewCompany(self):
        c = controller()
        self.assertEqual(c.addNewCompany('testcompany1',datetime.now(),1888.50), True)
        self.assertEqual(c.addNewCompany('testcompany2',datetime.now(),888.50), True)
	objects = c.listAllCompanies()
	for object in objects:
            print 'company: ' + object.company
            print 'date of quotation: ' + object.date_of_quote.strftime("%Y-%m-%d %H:%M%S")
            print 'total price: ' + str(object.total_price)
        #self.assertEqual(c.delCompany('testcompany'), True)

