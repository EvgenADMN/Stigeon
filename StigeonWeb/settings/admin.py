from django.contrib import admin
from .models import *

dbases = [PercoConnect, Devices, Employees, Colors]

for dbase in dbases:
    admin.site.register(dbase)