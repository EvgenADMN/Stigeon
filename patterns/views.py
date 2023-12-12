from django.shortcuts import render, redirect
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from psycopg2.errors import IntegrityError
from .models import *

Employees = apps.get_model('settings', 'Employees')
Devices = apps.get_model('settings', 'Devices')


def add(request):
    data = {
        'alert': '',
        'employees_list': [],
        'devices': Devices.objects.order_by('name'),
    }

    employees = Employees.objects.order_by('last_name')

    employees_list = []
    for employee in employees:
        if f'{employee.last_name} {employee.first_name} {employee.middle_name}' not in employees_list:
            data['employees_list'].append(f'{employee.last_name} {employee.first_name} {employee.middle_name}')

    if request.method == 'POST':
        params = {}
        for key, value in request.POST.items():
            params[key] = value

        try:
            Patterns.objects.get(name=params['name'])
            data['alert'] = 'Имя шаблона уже занято'
            return render(request, 'patterns/index.html', data)

        except ObjectDoesNotExist:
            Patterns.objects.create(name=params['name'],
                                    description=params['description'])
        for param in params:
            if 'chosen_device_' in param:
                Patterns_Devices.objects.create(pattern_name=Patterns.objects.get(name=params['name']),
                                                device_id=Devices.objects.get(id=params[param]))
            elif 'employee_' in param:
                for employee in employees:
                    if params[param] == f'{employee.last_name} {employee.first_name} {employee.middle_name}':
                        Patterns_Employees.objects.create(pattern_name=Patterns.objects.get(name=params['name']),
                                                          employee_id=Employees.objects.get(id=employee.id))

        data['alert'] = 'Шаблон успешно создан'
    return render(request, 'patterns/index.html', data)


def edit_menu(request):
    data = {
        'alert': '',
        'Patterns': Patterns.objects.order_by('name')
    }

    if request.method == 'POST':
        for k, v in request.POST.items():
            if k == 'editable-item':
                request.session['editable-item'] = v
                return redirect('patterns-edit')

    return render(request, 'patterns/edit-pattern-menu.html', data)


def edit(request):

    pattern = Patterns.objects.get(id=int(request.session['editable-item']))
    pattern_device = Patterns_Devices.objects.filter(pattern_name=pattern)
    pattern_employee = Patterns_Employees.objects.filter(pattern_name=pattern)
    employees = Employees.objects.order_by('last_name')

    data = {
        'alert': '',
        'Patterns': Patterns.objects.order_by('name'),
        'Pattern': pattern,
        'Pattern_Device': pattern_device,
        'Pattern_Employee': pattern_employee,
        'devices': Devices.objects.all(),
        'employees_list': employees
    }

    params = {}

    if request.method == 'POST':
        for key, value in request.POST.items():
            params[key] = value

        Patterns.objects.get(id=int(params['editable-pattern'])).delete()

        try:
            Patterns.objects.get(name=params['name'])
            data['alert'] = 'Имя шаблона уже занято'
            return render(request, 'patterns/edit-pattern.html', data)

        except ObjectDoesNotExist:
            Patterns.objects.create(name=params['name'],
                                    description=params['description'])
        for param in params:
            if 'chosen_device_' in param:
                Patterns_Devices.objects.create(pattern_name=Patterns.objects.get(name=params['name']),
                                                device_id=Devices.objects.get(id=params[param]))
            elif 'employee_' in param:
                for employee in employees:
                    if params[param] == f'{employee.last_name} {employee.first_name} {employee.middle_name}':
                        Patterns_Employees.objects.create(pattern_name=Patterns.objects.get(name=params['name']),
                                                          employee_id=Employees.objects.get(id=employee.id))

        return redirect('patterns-edit-menu')

    return render(request, 'patterns/edit-pattern.html', data)


def delete(request):
    data = {
        'alert': '',
        'Patterns': Patterns.objects.order_by()
    }

    if request.method == 'POST':
        params = {}
        for key, value in request.POST.items():
            print(f'{key}: {value}')
            params[key] = value
        try:
            Patterns.objects.get(id=int(params['deletable-item'])).delete()
            data['alert'] = 'Успешно удалено'
        except KeyError:
            pass

    return render(request, 'patterns/delete-pattern.html', data)


def periods(request):
    data = {
        'alert': '',
        'periods': Periods.objects.order_by('time_from'),
    }

    if request.method == 'POST':
        params = {}
        for key, value in request.POST.items():
            params[key] = value
            print(f'{key}: {value}')

        if 'add-period' in params:
            try:
                Periods.objects.create(time_from=params['time-from'],
                                       time_to=params['time-to'])
                data['alert'] = 'Успешно создано!'
            except IntegrityError:
                data['alert'] = 'Такой уже существует!'

        if 'edit-period' in params:
            try:
                editable = Periods.objects.get(id=params['editable-period'])
                editable.time_from = params['time-from']
                editable.time_to = params['time-to']
                editable.save()
                data['alert'] = 'Успешно изменено!'
            except:
                pass
        if 'delete-period' in params:
            try:
                Periods.objects.get(id=params['deletable-period']).delete()
                data['alert'] = 'Успешно удалено!'
            except:
                pass

    return render(request, 'patterns/periods.html', data)


def absenses(request):
    data = {
        'alert': '',
        'absenses': Absenses.objects.order_by('name'),
    }

    if request.method == 'POST':
        params = {}
        for key, value in request.POST.items():
            params[key] = value
            print(f'{key}: {value}')

        if 'add-absense' in params:
            try:
                Absenses.objects.get(name=params['name'])
                data['alert'] = 'Такая причина уже существует!'
            except IntegrityError:
                Absenses.objects.create(name=params['name'])
                data['alert'] = 'Успешно создано!'
        if 'edit-absense' in params:
            try:
                editable = Absenses.objects.get(id=params['editable-absense'])
                editable.name = params['name']
                editable.save()
                data['alert'] = 'Успешно изменено!'
            except KeyError:
                pass
        if 'delete-absense' in params:
            try:
                Absenses.objects.get(id=params['deletable-absense']).delete()
                data['alert'] = 'Успешно удалено!'
            except KeyError:
                pass

    return render(request, 'patterns/absenses.html', data)