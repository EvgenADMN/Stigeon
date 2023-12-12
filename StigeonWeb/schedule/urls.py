from django.urls import path, include
from .views import *

urlpatterns = [
    path('/', index, name='schedule'),
    path('/table', table, name='table'),
    path('/result', result, name='result'),
    path('/download', download, name='download')
]