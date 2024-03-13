from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index , name='home'),
    path('about-us/', views.about_us , name='about_us'),
    path('why-us/', views.whyus , name='whyus'),
    path('ourteam/', views.ourteam , name='ourteam'),
    path('contact/', views.contact , name='contact'),
    path('our-services/', views.our_services , name='our_services'),
    path('lawyer-profile/<str:profile_id>/', views.profile_view, name='profile_view'),

]
