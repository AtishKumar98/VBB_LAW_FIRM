from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index , name='home'),
    path('about_us/', views.about_us , name='about_us'),
    path('why_us/', views.whyus , name='whyus'),
    path('ourteam/', views.ourteam , name='ourteam'),
    path('contact/', views.contact , name='contact'),
    path('profile/<str:profile_id>/', views.profile_view, name='profile_view'),

]
