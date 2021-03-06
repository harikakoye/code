from __future__ import unicode_literals
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

class PropertyTypeCategoryTest(APITestCase):
    """ Test module for PropertyTypeCategory model """
    def setUp(self):
        PropertyTypeCategory.objects.create(title = 'Residential',description = 'water source')
    def test_propertytypecategory(self):
        url = baseurl+'/api/property_type_category/?title=Residential'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content), {u'msg': {}, u'status': u'success'})

class PropertyTypeTest(APITestCase):
    """ Test module for PropertyType model """
    def setUp(self):
        category = PropertyTypeCategory.objects.create(title = 'Residential',description = 'water source')
        PropertyType.objects.create(title = 'Villa',category = category)
    def test_propertytype(self):
        url = baseurl+'/api/property_type/?title=Villa'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content), [{u'id': 1, u'title': u'Villa'}])

class StateTest(APITestCase):
    """ Test module for State model """
    def setUp(self):
        State.objects.create(name = 'Telangana',country_code='IN')
    def test_state(self):
        url = baseurl+'/api/state/?name=Telangana'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),{u'msg': {u'state': [{u'id': 1, u'country_code': u'IN', u'name': u'Telangana'}]}, u'status': u'success'})

class RangeTest(APITestCase):
    """ Test module for Range model """
    def setUp(self):
        Range.objects.create(value = '5000000',name = 'plot')
    def test_range(self):
        url = baseurl+'/api/range/?name=plot'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'id': 1, u'value': 5000000, u'name': u'plot'}])

class HowSoonTest(APITestCase):
    """ Test module for HowSoon model """
    def setUp(self):
        HowSoon.objects.create(name ='30 days')
    def test_howsoon(self):
        url = baseurl+'/api/howsoon/?name=30 days'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'id': 1, u'name': u'30 days'}])

class MediaTest(APITestCase):
    """ Test module for Media model """
    def setUp(self):
        Media.objects.create(name ='core.jpg',path='documents',media_type='profilepics')
    def test_media(self):
        url = baseurl+'/api/upload_media/?name=30 days'
        data = {}
        response = self.client.post(url, data, format='json')
        print json.loads(response.content)
        #self.assertEqual(json.loads(response.content),{u'detail': u'Unsupported media type "application/json; charset=None" in request.'})

'''
class LocationTest(APITestCase):
    """ Test module for Location model """
    def setUp(self):
        Location.objects.create(formatted_address = 'Kukatpally, Hyderabad, Telangana, India', country = 'India', administrative_area_level_1 = 'Telangana',
            administrative_area_level_2='Ranga Reddy',sublocality_level_1='Kukatpally',sublocality_level_2='kukatpally 5th phase',
            locality='Hyderabad',raw='[{"long_name": "Kukatpally", "types": ["sublocality_level_1"]}, {"long_name": "Hyderabad", "types": ["locality"]}, {"long_name": "Ranga Reddy", "types": ["administrative_area_level_2"]}, {"long_name": "Telangana", "types": ["administrative_area_level_1"]}, {"long_name": "India", "types": ["country"]}]',
            lat='17.494793',lng='78.399644')
    def test_location(self):
        url = baseurl+'/api/location/?state=TELANGANA&key=beg'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        #self.assertEqual(json.loads(response.content), {u'msg': {u'city': [{u'city': u'hyderabad', u'state': 1, u'id': 1, u'name': u'begumpet'}]}, u'status': u'success'})
'''
