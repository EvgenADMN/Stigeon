from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='settings'),
    path('/get_devices', get_devices, name='get_devices'),
    path('/delete_device/<device_id>', delete_device, name='delete_device'),
    path('/get_employees', get_employees, name='get_employees'),
    path('/delete_employee/<employee_id>', delete_employee, name='delete_employee'),
]
