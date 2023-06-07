from django.urls import path
from django.views.generic import ListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ru/', views.home, name='home_ru'),
    path('en/', views.home, name='home_en'),

    path('contact/', views.contact, name='contact'),
    path('ru/contact/', views.contact, name='contact_ru'),
    path('en/contact/', views.contact, name='contact_en'),

    path('country/', views.country, name='country'),
    path('ru/country/', views.country, name='country_ru'),
    path('en/country/', views.country, name='country_en'),

    path('request/', views.request, name='request'),

    path('tourist-spot/', views.tourist_spot, name='tourist_spot'),
    path('ru/tourist-spot/', views.tourist_spot, name='tourist_spot_ru'),
    path('en/tourist-spot/', views.tourist_spot, name='tourist_spot_en'),

    path('tourist-spot/<int:pk>/', views.tourist_spot_detail, name='tourist_spot_detail'),
    path('ru/tourist-spot/<int:pk>/', views.tourist_spot_detail, name='tourist_spot_detail_ru'),
    path('en/tourist-spot/<int:pk>/', views.tourist_spot_detail, name='tourist_spot_detail_en'),

    path('object_detail/<int:pk>/', views.object_detail, name='object_detail'),
    path('ru/object_detail/<int:pk>/', views.object_detail, name='object_detail_ru'),
    path('en/object_detail/<int:pk>/', views.object_detail, name='object_detail_en'),

    path('guide/', views.guide, name='guide'),
    path('ru/guide/', views.guide, name='guide_ru'),
    path('en/guide/', views.guide, name='guide_en'),

]
