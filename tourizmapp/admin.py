from django.contrib import admin
from .models import *
from django.contrib import admin


@admin.register(Citys)
class CitysAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')
    list_display_links = ('id', 'name',)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'name', 'price')
    list_display_links = ('id', 'city', 'name',)


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'adult', 'child', 'hotel', 'date1', 'date2')

    list_display_links = ('id', 'name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text', 'subject')
    list_display_links = ('id', 'name',)


@admin.register(TourObjects)
class TourObjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


@admin.register(ObjectsDetail)
class ObjectsDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'city', 'language')
    list_display_links = ('id', 'first_name', 'last_name', )
