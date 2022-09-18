from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about_us, name='about_us'),
    path('our-team/', our_team, name='our_team'),
    path('our-history/', our_history, name='our_history'),
    path('faq/', faq, name='faq'),
    path('services-page/', services_page, name='services_page'),
    path('contact-us/', contact_us, name='contact_us'),
    path('pricing-plans/', pricing_plans, name='pricing_plans'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('startup-details/', startupdetails, name='startupdetails'),
    path('footernewsletter/', footernewsletter, name='footernewsletter'),
]
