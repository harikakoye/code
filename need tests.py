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

class NeedTest(APITestCase):
    maxDiff = None
    """ Test module for Need model """
    def setUp(self):
        location = Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')
        user = User.objects.create(first_name='harika',last_name='hamsini')
        customer = Customer.objects.create(user=user,dob = '1995-07-01',is_frequent_buyer = 'False')
        category = PropertyTypeCategory.objects.create(title = 'Commercial',description = 'power backup facility')
        propertytype = PropertyType.objects.create(title = 'Showroom',category = category)
        Need.objects.create(title='mfghjkh',need_type='land',status='active',desired_time='30 days',desired_budget_min=797887,desired_budget_max=997887,customer_notes ='bgjrhgjhn',location=location,propertytype=propertytype,customer=customer,is_expired='True')

    def test_need(self):
        url = baseurl+'/api/need/?title=mfghjkh'
        data = {}
        response = self.client.post(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),{u'msg': {u'expecting': u'title,need_type,status,desired_time,desired_budget_min,desired_budget_max,location,lat,lng,customer_id,propertytype_id'}, u'status': False})


class MatchedUserTest(APITestCase):
    maxDiff = None
    """ Test module for MatchedUser model """
    def setUp(self):
        location = Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')
        category = PropertyTypeCategory.objects.create(title = 'Commercial',description = 'power backup facility')
        propertytype = PropertyType.objects.create(title = 'Showroom',category = category)
        customer = Customer.objects.create(user_id=1,dob = '1995-07-01',is_frequent_buyer = 'False')
        need = Need.objects.create(title='mfghjkh',need_type='land',status='active',desired_time='30 days',desired_budget_min=797887,desired_budget_max=997887,customer_notes ='bgjrhgjhn',location=location,propertytype=propertytype,customer=customer,is_expired='True')
        user = User.objects.create(first_name='hamsini',last_name='hanvika')
        MatchedUser.objects.create(need=need,user=user,interested='True',engaged='False')
    def test_matcheduser(self):
        url = baseurl+'/api/match_user/?interested=True'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'need': 1, u'interested': True, u'engaged': False, u'id': 1, u'user': 1}])
