from django.urls import path, include
from.views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('settings', include('settings.urls')),
    path('patterns', include('patterns.urls')),
    path('schedule', include('schedule.urls')),
]
