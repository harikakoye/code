# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
# -*- coding: utf-8 -*-
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import *
from listing.models import *
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
# Create your tests here.
factory = APIRequestFactory()
baseurl='http://localhost:8000'

class BuilderTest(APITestCase):
    """ Test module for Builder model """
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
        media = Media .objects.create(name ='logo.jpg', path ='documents' ,media_type ='profilepics')
        user = User.objects.create(first_name='hamsini',last_name='hanvika')
        newbuilder = Builder.objects.create(user=user,company_name='polar it services',company_info='it is an internet portal dedicated to meet every aspect of the consumers needs in the real estate industry.It is a forum where buyers,sellers and brokers can exchange information, quickly, effectively and inexpensively.',company_website='goldpillar.com',rera_licence='abcdnh125xyz')
        newbuilder.contact_number.add(contact_number)
        newbuilder.contact_email.add(contact_email)
        newbuilder.address.add(address)
        newbuilder.media.add(media)
        newbuilder.location.add(location)
        newbuilder.save()
    def test_builder(self):
        url = baseurl+'/api/builder/?company_website=goldpillar.com'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'company_info': u'it is an internet portal dedicated to meet every aspect of the consumers needs in the real estate industry.It is a forum where buyers,sellers and brokers can exchange information, quickly, effectively and inexpensively.', u'contact_number': [{u'primary': False, u'id': 1, u'number': u'9704276592'}], u'company_name': u'polar it services', u'company_website': u'goldpillar.com', u'contact_email': [{u'primary': True, u'id': 1, u'email': u'hanvi@gmail.com'}], u'location': [{u'locality': u'Amaravathi', u'country': u'India', u'sublocality_level_2': u'Brodipet 3rd lane', u'raw': u'{"long_name": "Guntur", "types": ["sublocality_level_1"]}, {"long_name": "Amaravathi", "types": ["locality"]}, {"long_name": "Vijayawada", "types": ["administrative_area_level_2"]}, {"long_name": "Andhra Pradesh", "types": ["administrative_area_level_1"]}', u'administrative_area_level_2': u'Vijayawada', u'administrative_area_level_1': u'Andhra Pradesh', u'sublocality_level_1': u'Guntur', u'lat': u'16.314209', u'lng': u'80.435028', u'formatted_address': u'Brodipet, Guntur, Andhra Pradesh, India', u'id': 1}], u'address': [{u'city': u'Vijayawada', u'country': 1, u'pincode': 520010, u'line1': u'mg road', u'line2': u'40-1-48, Sri Krishna Sai Bhavan', u'lat': u'16.515099', u'state': 1, u'landmark': u'Opp. D.V.Manor Hotel, M.G.Road, Labbipet', u'lng': u'80.632095', u'id': 1}], u'id': 1, u'user': {u'username': u'', u'first_name': u'hamsini', u'last_name': u'hanvika', u'is_active': True, u'email': u'', u'is_superuser': False, u'is_staff': False, u'last_login': None, u'groups': [], u'user_permissions': [], u'password': u'', u'id': 1, u'date_joined': u'2017-12-28T09:54:35.408345Z'}}])

class AnnouncementTest(APITestCase):
    """ Test module for Announcement model """
    maxDiff = None
    def setUp(self):
        user = User.objects.create(first_name='hamsini',last_name='hanvika')
        newbuilder = Builder.objects.create(user=user,company_name='polar it services',company_info='it is an internet portal dedicated to meet every aspect of the consumers needs in the real estate industry.It is a forum where buyers,sellers and brokers can exchange information, quickly, effectively and inexpensively.',company_website='goldpillar.com',rera_licence='abcdnh125xyz')
        media = Media .objects.create(name ='logo.jpg', path ='documents' ,media_type ='profilepics')
        newannouncement = Announcement.objects.create(builder=newbuilder,announcement='coming soon')
        newannouncement.media.add(media)
        newannouncement.save()
    def test_announcement(self):
        url = baseurl+'/api/announcement/?announcement=coming soon'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'announcement': u'coming soon', u'builder': 1, u'id': 1, u'media': [1]}])

class VentureTest(APITestCase):
    """ Test module for Venture model """
    maxDiff = None
    def setUp(self):
        contact_number = ContactNumber.objects.create(number = '9704276592',primary = 'False')
        contact_email = ContactEmail.objects.create(email = 'hanvi@gmail.com',primary = 'True')
        category = PropertyTypeCategory.objects.create(title = 'Commercial',description = 'power backup facility')
        property_type = PropertyType.objects.create(title = 'Showroom',category = category)
        user = User.objects.create(first_name='hamsini',last_name='hanvika')
        newbuilder = Builder.objects.create(user=user,company_name='polar it services',company_info='it is an internet portal dedicated to meet every aspect of the consumers needs in the real estate industry.It is a forum where buyers,sellers and brokers can exchange information, quickly, effectively and inexpensively.',company_website='goldpillar.com',rera_licence='abcdnh125xyz')
        media = Media .objects.create(name ='logo.jpg', path ='documents' ,media_type ='profilepics')
        state = State.objects.create(name = 'Andhra Pradesh')
        country = Country.objects.create(name = 'India',country_code='IN',is_active='True')
        newventure = Venture.objects.create(state=state,country=country,builder=newbuilder,property_type=property_type,name='djangogoldpillar',status='active',total_units='69 sq.units',built_year='2015-07-01',pincode=868769,lat='18.314209',lng='82.435028')
        newventure.contact_number.add(contact_number)
        newventure.contact_email.add(contact_email)
        newventure.media.add(media)
        newventure.save()
    def test_venture(self):
        url = baseurl+'/api/venture/?name=djangogoldpillar'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        self.assertEqual(json.loads(response.content),[{u'status': u'active', u'city': u'', u'contact_number': [1], u'name': u'djangogoldpillar', u'country': 1, u'builder': 1, u'pincode': 868769, u'line1': u'', u'line2': u'', u'lat': u'18.314209', u'state': 1, u'contact_email': [1], u'total_units': u'69 sq.units', u'built_year': u'2015-07-01', u'media': [1], u'landmark': u'', u'lng': u'82.435028', u'property_type': 1, u'id': 1}])
'''
class BuilderListingTest(APITestCase):
    """ Test module for Builder model """
    maxDiff = None
    def setUp(self):
        state = State.objects.create(name = 'Andhra Pradesh')
        country = Country.objects.create(name = 'India',country_code='IN',is_active='True')
        category = PropertyTypeCategory.objects.create(title = 'Commercial',description = 'power backup facility')
        property_type = PropertyType.objects.create(title = 'Showroom',category = category)
        user = User.objects.create(first_name='hamsini',last_name='hanvika')
        newbuilder = Builder.objects.create(user=user,company_name='polar it services',company_info='it is an internet portal dedicated to meet every aspect of the consumers needs in the real estate industry.It is a forum where buyers,sellers and brokers can exchange information, quickly, effectively and inexpensively.',company_website='goldpillar.com',rera_licence='abcdnh125xyz')
        newventure = Venture.objects.create(state=state,country=country,builder=newbuilder,property_type=property_type,name='djangogoldpillar',status='active',total_units='69 sq.units',built_year='2015-07-01',pincode=868769,lat='18.314209',lng='82.435028')
        category = PropertyTypeCategory.objects.create(title = 'Residential',description = 'water source')
        propertytype = PropertyType.objects.create(title = 'Villa',category = category)

        config = Config.objects.create(title='hhjyhuk',description ='hjhgjj',unit='hjhgjhj',value='74657')
        amenities = Amenitie.objects.create(title='ghgfh',description ='ghg gfhgh')
        address = Address.objects.create(line1 = 'mg road',line2 = '40-1-48, Sri Krishna Sai Bhavan',landmark = 'Opp. D.V.Manor Hotel, M.G.Road, Labbipet',city = 'Vijayawada',state = state,country = country,pincode = 520010,lat='16.515099',lng='80.632095')
        location = Location.objects.create(formatted_address = 'Brodipet, Guntur, Andhra Pradesh, India', country = 'India', administrative_area_level_1 = 'Andhra Pradesh',
            administrative_area_level_2='Vijayawada',sublocality_level_1='Guntur',sublocality_level_2='Brodipet 3rd lane',
            locality='Amaravathi',raw='{"long_name": "Guntur", "types": ["sublocality_level_1"]}, {"long_name": "Amaravathi", "types": ["locality"]}, {"long_name": "Vijayawada", "types": ["administrative_area_level_2"]}, {"long_name": "Andhra Pradesh", "types": ["administrative_area_level_1"]}',
            lat='16.314209',lng='80.435028')
        transactiontype = Transactiontype.objects.create(name ='rent')
        listing = Listing.objects.create(title='ghgfhgf',user=user,location=location,address=address,propertytype=propertytype,transactiontype=transactiontype,property_ownership='hghti',description='hghgh',
                                        society_name='ggfg',built_year=1999-08-15,posted_by='fdgfdg',listing_status='gfdgfdg',occupancy_status='fgjgf',available_from_month=07,available_from_year=2019,
                                        engage_agents='True',is_expired='False',expected_price=1200000,show_price_as=2900000,price_per_sqft=30000,maintanence_charges=6899,duration ='30 days',expected_rent_price=876856)
        newbuilderlisting = BuilderListing(builder=newbuilder,venture =newventure,property_type=property_type,price_min=5300000,price_max=8100000,avilable_units=44,description='hjhgjh',features='hjhjghgh')
        newbuilderlisting.listing.add(listing)
        newbuilderlisting.save()
        newconfig.propertytype.add(property_type)
        listing.amenities.add(amenities)
        listing.config.add(config)
        newconfig.propertytype.save()
    def test_builderlisting(self):
        url = baseurl+'/api/builderlisting/?name=djangogoldpillar'
        data = {}
        response = self.client.get(url, data, format='json')
        print json.loads(response.content)
        #self.assertEqual(json.loads(response.content),[{u'price_max': 8100000, u'avilable_units': 44, u'features': u'hjhjghgh', u'builder': 1, u'price_min': 5300000, u'venture': 1, u'listing': [], u'property_type': 1, u'id': 1, u'description': u'hjhgjh'}])
'''
