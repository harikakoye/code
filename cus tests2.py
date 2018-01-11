
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
#from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
#from rest_framework.test import APIClient
#from rest_framework.test import APIRequestFactory
from django.test import RequestFactory
from rest_framework.test import APITestCase
from .models import *
from core.models import *
from .views import*
# Create your tests here.

baseurl='http://localhost:8000'

class CustomerViewSetTest(APITestCase):
    maxDiff = None
    """ Test module for Customer model """
    def test_customer(self):
        contact_number = ContactNumber.objects.create(number = '9908201775',primary = 'True')
        contact_email = ContactEmail.objects.create(email = 'hamsini@gmail.com',primary = 'False')
        location = Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')
        newuser = User.objects.create(first_name='harika',last_name="hamsini",username="test",password="12345")
        newcustomer = Customer.objects.create(user=newuser,is_frequent_buyer = 0)
        newcustomer.contact_number.add(contact_number)
        newcustomer.contact_email.add(contact_email)
        newcustomer.location.add(location)
        newcustomer.save()
        url = baseurl+'/api/customer/registration/?'
        data = {}
        data['otp'] = 306673
        data['first_name'] = "Harika"
        data["contact_number"] = "9908201775"
        data["locations"] = "location"
        response = self.client.post(url, data, format='json')
        print json.loads(response.content)
        #self.assertEqual(json.loads(response.content),)

