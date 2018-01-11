
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

class RegistrationTest(APITestCase):
    maxDiff = None
    """ Test module for Customer model """
    def test_registration(self):
        contact_number = ContactNumber.objects.create(number = '9133048409',primary = 'True')
        contact_email = ContactEmail.objects.create(email = 'hamsini@gmail.com',primary = 'False')
        location = Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')
        state = State.objects.create(name = 'Andhra Pradesh')
        country = Country.objects.create(name = 'India',country_code='IN',is_active='True')
        address = Address.objects.create(line1 = 'mg road',line2 = '40-1-48, Sri Krishna Sai Bhavan',landmark = 'Opp. D.V.Manor Hotel, M.G.Road, Labbipet',city = 'Vijayawada',state = state,country = country,pincode = 520010,lat='16.515099',lng='80.632095')
        newuser = User.objects.create(first_name='harika',last_name="hamsini",username="test",password="12345")
        newbuilder = Builder.objects.create(user=newuser)
        newbuilder.contact_number.add(contact_number)
        newbuilder.contact_email.add(contact_email)
        newbuilder.location.add(location)
        newbuilder.address.add(address)
        newbuilder.save()
        url = baseurl+'/api/builder/registration/?'
        data = {}
        data['otp'] = 306673
        data['first_name'] = "Harika"
        data['last_name'] = "Hamsini"
        data["contact_number"] = "9908201775"
        data["locations"] = [{"location":[{"long_name":"Prakash Nagar","short_name":"Prakash Nagar","types":["sublocality_level_3","sublocality","political"]},{"long_name":"Bhagat Singh II","short_name":"Bhagat Singh II","types":["sublocality_level_2","sublocality","political"]},{"long_name":"Jogeshwari West","short_name":"Jogeshwari West","types":["sublocality_level_1","sublocality","political"]},{"long_name":"Mumbai","short_name":"Mumbai","types":["locality","political"]},{"long_name":"Mumbai Suburban","short_name":"Mumbai Suburban","types":["administrative_area_level_2","political"]},{"long_name":"Maharashtra","short_name":"MH","types":["administrative_area_level_1","political"]},{"long_name":"India","short_name":"IN","types":["country","political"]},{"long_name":"400047","short_name":"400047","types":["postal_code"]}],
        "lat":19.1547349,
        "lng":72.83472089999998,
        "formatted_address":"Prakash Nagar, Bhagat Singh II, Jogeshwari West, Mumbai, Maharashtra 400047, India"
        },{"location": [{"long_name":"Mumbai","short_name":"Mumbai","types":["locality","political"]},{"long_name":"Mumbai Suburban","short_name":"Mumbai Suburban","types":["administrative_area_level_2","political"]},{"long_name":"Maharashtra","short_name":"MH","types":["administrative_area_level_1","political"]},{"long_name":"India","short_name":"IN","types":["country","political"]},{"long_name":"400099","short_name":"400099","types":["postal_code"]}],
        "lat":19.0895595,
        "lng":72.8656144,
        "formatted_address":"Mumbai, Maharashtra 400099, India"
        }],
        data["company_name"]=''
        data["company_website"]=''
        response = self.client.post(url, data, format='json')
        print json.loads(response.content)
        #self.assertEqual(json.loads(response.content),)

