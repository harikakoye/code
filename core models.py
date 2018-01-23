# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import uuid

from django.utils import timezone


STATUS_CHOICES = (
    ('new','New'),
    ('agent_responded', 'Agent Responded'),
    ('agent_engaged', 'Agent Engaged'),
    ('deal_done', 'Deal Done'),
    ('close', 'Close')
)

class Country(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=0)
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class ConfirmOTP(models.Model):
    user = models.ForeignKey(User,related_name="new_user")
    temp = models.CharField(max_length=255)

class Range(models.Model):
    value = models.IntegerField()
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name.lower()

class HowSoon(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name.lower()

class TransactionType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name.lower()

class UserDeviceToken(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=500)
    deviceinfo = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return (self.user.username)+" - "+(self.token)

# class UserToken(models.Model):
#     user_id = models.IntegerField()
#     token = models.CharField(max_length=255, default=uuid.uuid4 ,unique=True, null= True)

    # def __init__(self):
    #     super(UserToken, self).__init__()
    #     self.token = uuid.uuid4().hex



class ContactEmail(models.Model):
    email = models.EmailField()
    primary = models.BooleanField(default=False)
    def __str__(self):
        return self.email


class SystemConfig(models.Model):
    parameter = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.parameter+" - "+ self.value


class ContactNumber(models.Model):
    number = models.CharField(max_length=25)
    primary = models.BooleanField(default=False)
    def __str__(self):
        return self.PropertyTypeCategorynumber


class Address(models.Model):
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State)
    country = models.ForeignKey(Country)
    pincode = models.IntegerField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return self.line1+" - "+self.city

class Location(models.Model):
    formatted_address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    administrative_area_level_1 = models.CharField(max_length=255)
    administrative_area_level_2 = models.CharField(max_length=255)
    sublocality_level_1 = models.CharField(max_length=255)
    sublocality_level_2 = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    raw = models.TextField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return self.formatted_address

class PropertyTypeCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Unit(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class OccupancyStatus(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class PropertyType(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PropertyTypeCategory)
    def __str__(self):
        return self.title

class Media(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255,default="")
    media_type = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Review(models.Model):
    from_user = models.ForeignKey(User,related_name="from_user")
    to_user = models.ForeignKey(User,related_name="to_user")
    review = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return self.review


class Amenitie(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255,default="")
    description = models.TextField(default="")
    def __str__(self):
        return self.title
#
# class PaytmHistory(models.Model):
#     user = models.ForeignKey(User)
#     ORDERID = models.CharField('ORDER ID', max_length=30)
#     TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
#     TXNID = models.IntegerField('TXN ID')
#     BANKTXNID = models.IntegerField('BANK TXN ID', null=True, blank=True)
#     BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
#     RESPCODE = models.IntegerField('RESP CODE')
#     PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
#     CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
#     GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
#     MID = models.CharField(max_length=40)
#     RESPMSG = models.TextField('RESP MSG', max_length=250)
#     TXNAMOUNT = models.FloatField('TXN AMOUNT')
#     STATUS = models.CharField('STATUS', max_length=12)
#
#     def __unicode__(self):
#         return self.STATUS

admin.site.register(UserDeviceToken)
admin.site.register(SystemConfig)
admin.site.register(ContactNumber)
admin.site.register(ContactEmail)
admin.site.register(Address)
admin.site.register(Location)
admin.site.register(Media)
#admin.site.register(Unit)<
#admin.site.register(OccupancyStatus)<
#admin.site.register(Review)
admin.site.register(ConfirmOTP)
#admin.site.register(Amenitie)<
#admin.site.register(State)
#admin.site.register(Range)<
#admin.site.register(Country)
#admin.site.register(HowSoon)<
#admin.site.register(TransactionType)<
#admin.site.register(PropertyTypeCategory)<
#admin.site.register(PropertyType)<

# admin.site.register(PaytmHistory)


admin.site.site_header = 'Gold Pillar'
