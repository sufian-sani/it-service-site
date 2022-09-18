from django.urls import path
from .views import *

app_name = 'digitalmarketing'

urlpatterns = [
    path('seo-service-details/', seo_service_details, name='seo_service_details'),
    path('seo-service-details/<slug>/', protfolio_details, name='protfolio_details'),
]
