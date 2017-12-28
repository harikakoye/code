# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
# -*- coding: utf-8 -*-
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import *
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
# Create your tests here.
factory = APIRequestFactory()
baseurl='http://localhost:8000'

class AgentTest(APITestCase):
    """ Test module for Agent model """
    maxDiff = None
    def setUp(self):
        contact_number = ContactNumber.objects.create(number = '9704276592',primary = 'False')
        contact_email = ContactEmail.objects.create(email = 'hanvi@gmail.com',primary = 'True')
        state = State.objects.create(name = 'Andhra Pradesh')
        country = Country.objects.create(name = 'India',country_code='IN',is_active='True')
        address = Address.objects.create(line1 = 'mg road',line2 = '40-1-48, Sri Krishna Sai Bhavan',landmark = 'Opp. D.V.Manor Hotel, M.G.Road, Labbipet',city = 'Vijayawada',state = state,country = country,pincode = 520010,lat='16.515099',lng='80.632095')
        location = Location.objects.create(formatted_address = 'Brodipet, Guntur, Andhra Pradesh, India', country = 'India', administrative_area_level_1 = 'Andhra Pradesh',
            administrative_area_level_2='Vijayawada',sublocality_level_1='Guntur',sublocality_level_2='Brodipet 3rd lane',
            locality='Amaravathi',raw='{"long_name": "Guntur", "types": ["sublocality_level_1"]}, {"long_name": "Amaravathi", "types": ["locality"]}, {"long_name": "Vijayawada", "types": ["administrative_area_level_2"]}, {"long_name": "Andhra Pradesh", "types": ["administrative_area_level_1"]}',
            lat='16.314209',lng='80.435028')

        category = PropertyTypeCategory.objects.create(title = 'Commercial',description = 'power backup facility')
        specialization = PropertyType.objects.create(title = 'Showroom',category = category)
        media = Media .objects.create(name ='logo.jpg', path ='documents' ,media_type ='profilepics')
        user = User.objects.create(first_name='hamsini',last_name='hanvika')
        from_user = User.objects.create(username = 7775554891)
        to_user = User.objects.create(username = 9994447771)
        review = Review.objects.create(from_user = from_user,to_user = to_user,review = 'good',rating = '3')
        newagent = Agent.objects.create(user=user,dob = '2005-11-02',education = 'b.tech',company_name = 'tagontech',
            experience = '5',agent_notes = 'expert in selling the flats,lands',rera_licence='abcd123xyz')
        newagent.contact_number.add(contact_number)
        newagent.contact_email.add(contact_email)
        newagent.address.add(address)
        newagent.location.add(location)
        newagent.review.add(review)
        newagent.media.add(media)
        newagent.specialization.add(specialization)
        newagent.save()
    def test_agent(self):
        url = baseurl+'/api/agent/?dob = 2005-11-02'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'contact_number': [{u'primary': False, u'id': 1, u'number': u'9704276592'}], u'specialization': [{u'id': 1, u'title': u'Showroom'}], u'dob': u'2005-11-02', u'media': [{u'path': u'documents', u'id': 1, u'media_type': u'profilepics', u'name': u'logo.jpg'}], u'review': [{u'to_user': 3, u'rating': 3, u'review': u'good', u'id': 1, u'from_user': 2}], u'experience': u'5', u'company_name': u'tagontech', u'contact_email': [{u'primary': True, u'id': 1, u'email': u'hanvi@gmail.com'}], u'user': {u'username': u'', u'first_name': u'hamsini', u'last_name': u'hanvika', u'is_active': True, u'email': u'', u'is_superuser': False, u'is_staff': False, u'last_login': None, u'groups': [], u'user_permissions': [], u'password': u'', u'id': 1, u'date_joined': u'2017-12-28T09:50:20.831495Z'}, u'address': [{u'city': u'Vijayawada', u'country': 1, u'pincode': 520010, u'line1': u'mg road', u'line2': u'40-1-48, Sri Krishna Sai Bhavan', u'lat': u'16.515099', u'state': 1, u'landmark': u'Opp. D.V.Manor Hotel, M.G.Road, Labbipet', u'lng': u'80.632095', u'id': 1}], u'education': u'b.tech', u'id': 1, u'agent_notes': u'expert in selling the flats,lands', u'location': [{u'locality': u'Amaravathi', u'country': u'India', u'sublocality_level_2': u'Brodipet 3rd lane', u'raw': u'{"long_name": "Guntur", "types": ["sublocality_level_1"]}, {"long_name": "Amaravathi", "types": ["locality"]}, {"long_name": "Vijayawada", "types": ["administrative_area_level_2"]}, {"long_name": "Andhra Pradesh", "types": ["administrative_area_level_1"]}', u'administrative_area_level_2': u'Vijayawada', u'administrative_area_level_1': u'Andhra Pradesh', u'sublocality_level_1': u'Guntur', u'lat': u'16.314209', u'lng': u'80.435028', u'formatted_address': u'Brodipet, Guntur, Andhra Pradesh, India', u'id': 1}]}])

class ReferenceTest(APITestCase):
    """ Test module for Reference model """
    def setUp(self):
        contact_number = ContactNumber.objects.create(number = '847547908',primary = 'True')
        user = User.objects.create(first_name='harika',last_name='hanvi')
        agent = Agent.objects.create(user=user,dob = '2005-11-02',education = 'b.tech',company_name = 'tagontech',
            experience = '5',agent_notes = 'expert in selling the flats,lands',rera_licence='abcd123xyz')
        newreference = Reference.objects.create(first_name='hanvika',last_name='hanvi',remark='bad',agent=agent)
        newreference.contact_number.add(contact_number)
    def test_reference(self):
        url = baseurl+'/api/reference/?first_name = hanvika'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'remark': u'bad', u'last_name': u'hanvi', u'first_name': u'hanvika', u'agent': 1, u'contact_number': [1], u'id': 1}])
