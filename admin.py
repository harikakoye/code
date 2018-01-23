# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from core.models import *

class PropertyTypeResource(resources.ModelResource):
    class Meta:
        model = PropertyType
class PropertyTypeCategoryResource(resources.ModelResource):
    class Meta:
        model = PropertyTypeCategory
class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
class TransactionTypeResource(resources.ModelResource):
    class Meta:
        model = TransactionType
class HowSoonResource(resources.ModelResource):
    class Meta:
        model = HowSoon
class RangeResource(resources.ModelResource):
    class Meta:
        model = Range
class StateResource(resources.ModelResource):
    class Meta:
        model = State
class AmenitieResource(resources.ModelResource):
    class Meta:
        model = Amenitie
class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review
class ContactNumberResource(resources.ModelResource):
    class Meta:
        model = ContactNumber
class ContactEmailResource(resources.ModelResource):
    class Meta:
        model = ContactEmail
class AddressResource(resources.ModelResource):
    class Meta:
        model = Address
class LocationResource(resources.ModelResource):
    class Meta:
        model = Location

class PropertyTypeAdmin(ImportExportModelAdmin):
    resource_class = PropertyTypeResource
class PropertyTypeCategoryAdmin(ImportExportModelAdmin):
    resource_class = PropertyTypeCategoryResource
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
class TransactionTypeAdmin(ImportExportModelAdmin):
    resource_class = TransactionTypeResource
class HowSoonAdmin(ImportExportModelAdmin):
    resource_class = HowSoonResource
class RangeAdmin(ImportExportModelAdmin):
    resource_class = RangeResource
class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource
class AmenitieAdmin(ImportExportModelAdmin):
    resource_class = AmenitieResource
class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource
class ContactNumberAdmin(ImportExportModelAdmin):
    resource_class = ContactNumberResource
class ContactEmailAdmin(ImportExportModelAdmin):
    resource_class = ContactEmailResource
class AddressAdmin(ImportExportModelAdmin):
    resource_class = AddressResource
class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource

admin.site.register(PropertyType,PropertyTypeAdmin)
admin.site.register(PropertyTypeCategory,PropertyTypeCategoryAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(TransactionType,TransactionTypeAdmin)
admin.site.register(HowSoon,HowSoonAdmin)
admin.site.register(Range,RangeAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(Amenitie,AmenitieAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(ContactNumber,ContactNumberAdmin)
admin.site.register(ContactEmail,ContactEmailAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Location,LocationAdmin)
