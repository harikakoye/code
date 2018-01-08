
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .models import *
from core.models import *
from .views import*
# Create your tests here.
factory = APIRequestFactory()
baseurl='http://localhost:8000'

class CustomerViewSetTest(APITestCase):
    maxDiff = None
    """ Test module for Customer model """
    def setUp(self):
        contact_number = ContactNumber.objects.create(number = '9010272300',primary = 'True')
        contact_email = ContactEmail.objects.create(email = 'hamsini@gmail.com',primary = 'False')
        #state = State.objects.create(name = 'Telangana',country_code='IN')
        #country = Country.objects.create(name = 'India',country_code='IN',is_active='True')
        #address = Address.objects.create(line1 = 'prakash nagar',line2 = 'ial colony',landmark = '3rd lane',city = 'Secunderabad',state = state,country = country,pincode = '500003',lat='20.0',lng='77.0')
        location = Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')
        newuser = User.objects.create(first_name='harika',last_name="hamsini",username="test",password="12345",otp=717711)
        newcustomer = Customer.objects.create(user=newuser,is_frequent_buyer = 0)
        newcustomer.contact_number.add(contact_number)
        newcustomer.contact_email.add(contact_email)
        #newcustomer.address.add(address)
        newcustomer.location.add(location)
        newcustomer.save()
        #print newcustomer
    def test_customer(self):
        url = baseurl+'/api/customer/registration/?'
        data = {}
        response = self.client.post(url, data, format='json')
        print json.loads(response.content)
        #self.assertEqual(json.loads(response.content),{u'msg': {u'expecting': u'first_name,contact_number,locations,otp'}, u'status': False})

