from django.urls import path, include
from .views import *

urlpatterns = [
    path('/add', add, name='patterns-add'),
    path('/edit_pattern', edit, name='patterns-edit'),
    path('/edit', edit_menu, name='patterns-edit-menu'),
    path('/delete', delete, name='patterns-del'),
    path('/periods', periods, name='periods'),
    path('/absenses', absenses, name='absenses'),
]