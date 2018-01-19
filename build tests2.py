
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.test import TestCase, Client
from django.urls import reverse
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
        contact_number = ContactNumber.objects.create(number = '9908201775',primary = 'True')
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
        #verify otp code
        vurl = baseurl+'/api/verify/'
        vdata = {}
        vdata['number'] = '9133048409'
        vresponse = self.client.post(vurl, vdata, format='json')
        ##registration
        url = baseurl+'/api/builder/registration/?'
        data = {}
        otp = input('Enter otp :')
        data['otp'] = otp
        data['first_name'] = "Harika"
        data['last_name'] = "Hamsini"
        data["contact_number"] = "9133048409"

        data["locations"] = [{
	"location": [{
		"long_name": "Prakash Nagar",
		"short_name": "Prakash Nagar",
		"types": ["sublocality_level_3", "sublocality", "political"]
	}, {
		"long_name": "Bhagat Singh II",
		"short_name": "Bhagat Singh II",
		"types": ["sublocality_level_2", "sublocality", "political"]
	}, {
		"long_name": "Jogeshwari West",
		"short_name": "Jogeshwari West",
		"types": ["sublocality_level_1", "sublocality", "political"]
	}, {
		"long_name": "Mumbai",
		"short_name": "Mumbai",
		"types": ["locality", "political"]
	}, {
		"long_name": "Mumbai Suburban",
		"short_name": "Mumbai Suburban",
		"types": ["administrative_area_level_2", "political"]
	}, {
		"long_name": "Maharashtra",
		"short_name": "MH",
		"types": ["administrative_area_level_1", "political"]
	}, {
		"long_name": "India",
		"short_name": "IN",
		"types": ["country", "political"]
	}, {
		"long_name": "400047",
		"short_name": "400047",
		"types": ["postal_code"]
	}],
	"lat": 19.1547349,
	"lng": 72.83472089999998,
	"formatted_address": "Prakash Nagar, Bhagat Singh II, Jogeshwari West, Mumbai, Maharashtra 400047, India"
}]

        data["company_website"] = 'tagontech.com'
        data["company_name"] = 'tagon software technologies'

        response = self.client.post(url, data, format='json')
        print json.loads(response.content)
        responseData = json.loads(response.content)
        self.assertEqual(responseData['status'],'success')
        self.assertEqual(responseData['msg']['company_website'],'tagontech.com')
        self.assertEqual(responseData['msg']['company_name'],'tagon software technologies')
        self.assertEqual(responseData['msg']['location'],[{u'sublocality_level_1': u'Jogeshwari West', u'administrative_area_level_2': u'Mumbai Suburban', u'administrative_area_level_1': u'Maharashtra', u'locality': u'Mumbai', u'lat': u'19.154735', u'country': u'', u'sublocality_level_2': u'Bhagat Singh II', u'formatted_address': u'Prakash Nagar, Bhagat Singh II, Jogeshwari West, Mumbai, Maharashtra 400047, India', u'lng': u'72.834721', u'id': 2}])
        self.assertEqual(responseData['msg']['contact_number'],[{u'number': u'9133048409', u'primary': True, u'id': 2}])
        #self.assertEqual(responseData['msg']['user'],{u'username': u'9133048409', u'last_name': u'Hamsini', u'is_active': False, u'is_staff': False, u'groups': [], u'user_permissions': [], u'password': u'', u'id': 2, u'date_joined': u'2018-01-19T05:24:04.775955Z', u'first_name': u'Harika', u'is_superuser': False, u'last_login': None, u'email': u''})

