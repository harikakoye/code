
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
# Create your tests here.
factory = APIRequestFactory()
baseurl='http://localhost:8000'

class CustomerTest(APITestCase):
    maxDiff = None
    """ Test module for Location model """
    def setUp(self):
        contact_number = ContactNumber.objects.create(number = '8885556666',primary = 'True')
        contact_email = ContactEmail.objects.create(email = 'hamsini@gmail.com',primary = 'False')
        user = User.objects.create(first_name='harika',last_name='hamsini')
        state = State.objects.create(name = 'Telangana',country_code='IN')
        country = Country.objects.create(name = 'India',country_code='IN',is_active='True')
        address = Address.objects.create(line1 = 'prakash nagar',line2 = 'ial colony',landmark = '3rd lane',city = 'Secunderabad',state = state,country = country,pincode = '500003',lat='20.0',lng='77.0')
        location = Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')

        newcustomer = Customer.objects.create(user=user,dob = '1995-07-01',is_frequent_buyer = 'False')
        newcustomer.contact_number.add(contact_number)
        newcustomer.contact_email.add(contact_email)
        newcustomer.address.add(address)
        newcustomer.location.add(location)
        newcustomer.save()
    def test_customer(self):
        url = baseurl+'/api/customer/?dob=1995-07-01'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'contact_number': [{u'primary': True, u'id': 1, u'number': u'8885556666'}], u'dob': u'1995-07-01', u'media': None, u'is_frequent_buyer': False, u'contact_email': [{u'primary': False, u'id': 1, u'email': u'hamsini@gmail.com'}], u'user': {u'username': u'', u'first_name': u'harika', u'last_name': u'hamsini', u'url': u'http://testserver/api/user/1/', u'is_active': True, u'is_superuser': False, u'is_staff': False, u'last_login': None, u'groups': [], u'user_permissions': [], u'password': u'', u'email': u'', u'date_joined': u'2017-12-21T10:12:23.308057Z'}, u'address': [{u'city': u'Secunderabad', u'country': 1, u'pincode': 500003, u'line1': u'prakash nagar', u'line2': u'ial colony', u'lat': u'20.000000', u'state': 1, u'landmark': u'3rd lane', u'lng': u'77.000000', u'id': 1}], u'id': 1, u'location': [{u'locality': u'Hyderabad', u'country': u'India', u'sublocality_level_2': u'kukatpally 5th phase', u'raw': u'[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]', u'administrative_area_level_2': u'Ranga Reddy', u'administrative_area_level_1': u'Telangana', u'sublocality_level_1': u'Kukatpally', u'lat': u'17.494793', u'lng': u'78.399644', u'formatted_address': u'Kukatpally, Hyderabad, Telangana, India', u'id': 1}]}])
