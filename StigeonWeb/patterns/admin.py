from django.contrib import admin
from .models import *

dbases = [Patterns, Patterns_Devices, Patterns_Employees, Periods, Absenses]

for dbase in dbases:
    admin.site.register(dbase)
