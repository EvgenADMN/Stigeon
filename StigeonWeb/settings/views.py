import time
from pprint import pprint

from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import *
import win32com.client as w32
import pythoncom


def connect(data, host, port, login, password, sdk_name):
    pythoncom.CoInitialize()
    com = w32.Dispatch(sdk_name)
    connection = com.SetConnect(host, port, login, password)

    if connection == 0:
        data['alert'] = 'Подключено успешно!'
        return com
    else:
        data['alert'] = 'Подключение не удалось.\nПроверьте настройки подключения'


def fill_device_list():
    with open('settings/files/devices.xml', encoding='UTF8') as file:
        devices_list = [i.split('"') for i in file.read().split('><') if 'ipaddres' in i]

    devices = []
    counter = 0
    for device in devices_list:
        temp = {}
        for j in device:
            try:
                if ' ' in device[counter]:
                    temp[device[counter].split(' ')[1].replace('=', '')] = device[counter + 1]
                elif device[counter] != '':
                    temp[device[counter].replace('=', '')] = device[counter + 1]
                counter += 2
            except IndexError:
                pass
        devices.append(temp)
        counter = 0

    for device in devices:
        try:
            Devices.objects.create(name=device['displayname'],
                                   host=device['ipaddres'],
                                   gateway=device['ipgate'],
                                   netmask=device['netmask'],
                                   mac=device['macaddres'],
                                   id_internal=device['id_internal'])
        except IntegrityError:
            pass


def show_device_list(data):
    data['devices'] = [i for i in Devices.objects.order_by('name', 'host')]


def fill_employee_list():
    with open('settings/files/employees.xml', encoding='UTF8') as file:
        employee_raw = [i.split('"') for i in file.read().split('><') if 'first_name' in i]

    employees = []
    counter = 0
    for employee in employee_raw:
        param = {}
        for j in employee:
            try:
                if ' ' in employee[counter]:
                    param[employee[counter].split(' ')[1].replace('=', '')] = employee[counter + 1]
                elif employee[counter] != '':
                    param[employee[counter].replace('=', '')] = employee[counter + 1]
                counter += 2
            except IndexError:
                pass
        employees.append(param)
        counter = 0

    for employee in employees:
        try:
            Employees.objects.create(last_name=employee['last_name'],
                                     first_name=employee['first_name'],
                                     middle_name=employee['middle_name'],
                                     id_internal=employee['id_internal'])
        except IntegrityError:
            pass


def show_employees_list(data):
    data['employees'] = [i for i in Employees.objects.order_by('last_name', 'first_name')]


# ======================


def index(request):
    data = {
        'alert': '',
        'colors': {
            'absenteeism': '',
            'lateness': '',
            'early': '',
            'lateness_early': '',
            'purpose': ''
        },
    }

    try:
        colors = Colors.objects.all()[0]
        data['colors']['absenteeism'] = colors.absenteeism
        data['colors']['lateness'] = colors.lateness
        data['colors']['early'] = colors.early
        data['colors']['lateness_early'] = colors.lateness_early
        data['colors']['purpose'] = colors.purpose

    except IndexError:
        Colors.objects.create(absenteeism='#ff8085',
                              lateness='#ffd99a',
                              early='#9ab8ff',
                              lateness_early='#dbf7a2',
                              purpose='#c7ffd8')
        colors = Colors.objects.get()
        data['colors']['absenteeism'] = colors.absenteeism
        data['colors']['lateness'] = colors.lateness
        data['colors']['early'] = colors.early
        data['colors']['lateness_early'] = colors.lateness_early
        data['colors']['purpose'] = colors.purpose

    if request.method == 'POST':
        params = {}
        for key, value in request.POST.items():
            params[key] = value

        if 'action' in params:
            if params['action'] == 'check-connection':
                connection = PercoConnect.objects.all()[0]
                com = connect(data, connection.host, connection.port, connection.login,
                              connection.password, connection.sdk_name)
            elif params['action'] == 'save-connection':
                PercoConnect.objects.all().delete()
                PercoConnect.objects.create(host=params['host'],
                                            port=params['port'],
                                            login=params['login'],
                                            password=params['password'],
                                            sdk_name=params['sdk_name'])
                data['alert'] = 'Успешно сохранено. Нажмите кнопку "Проверить подключение"'

                return render(request, 'settings/index.html', data)

        elif 'delete_selected_devices' in params:
            for param in params:
                if 'checkbox_' not in param:
                    continue
                Devices.objects.get(id=params[param]).delete()

        elif 'delete_selected_employees' in params:
            for param in params:
                if 'checkbox_' not in param:
                    continue
                Employees.objects.get(id=params[param]).delete()

        elif 'colors' in params:
            pprint(params)
            colors = Colors.objects.get()
            colors.absenteeism = params['absenteeism']
            colors.lateness = params['lateness']
            colors.early = params['early']
            colors.lateness_early = params['lateness_early']
            colors.purpose = params['purpose']
            colors.save()

            data['colors']['absenteeism'] = colors.absenteeism
            data['colors']['lateness'] = colors.lateness
            data['colors']['early'] = colors.early
            data['colors']['lateness_early'] = colors.lateness_early
            data['colors']['purpose'] = colors.purpose

    show_device_list(data)
    show_employees_list(data)

    return render(request, 'settings/index.html', data)


def get_devices(request):
    connection = PercoConnect.objects.all()[0]
    com = connect({}, connection.host, connection.port, connection.login,
                  connection.password, connection.sdk_name)

    XML_DOM = w32.Dispatch('Microsoft.XMLDOM')
    Header = XML_DOM.createProcessingInstruction('xml', 'version="1.0" encoding="UTF-8" standalone="yes"')
    XML_DOM.appendChild(Header)

    Elem = XML_DOM.createElement("documentrequest")
    Elem.setAttribute("type", "config")
    XML_DOM.appendChild(Elem)

    com.GetData(XML_DOM)
    XML_DOM.save('settings/files/devices.xml')
    fill_device_list()
    return redirect('settings')


def delete_device(request, device_id):
    Devices.objects.get(id=device_id).delete()
    return redirect('settings')


def get_employees(request):
    connection = PercoConnect.objects.all()[0]
    com = connect({}, connection.host, connection.port, connection.login,
                  connection.password, connection.sdk_name)

    XML_DOM = w32.Dispatch('Microsoft.XMLDOM')
    Header = XML_DOM.createProcessingInstruction('xml', 'version="1.0" encoding="UTF-8" standalone="yes"')
    XML_DOM.appendChild(Header)

    Elem = XML_DOM.createElement("documentrequest")
    Elem.setAttribute("type", "staff")
    Elem.setAttribute("mode_display", "employ")
    Elem.setAttribute("subdiv", "")
    Elem.setAttribute("get_photo", "false")
    Elem.setAttribute("get_sms_phone_data", "false")
    Elem.setAttribute("get_addition_data", "false")
    Elem.setAttribute("get_document_data", "false")
    XML_DOM.appendChild(Elem)

    com.GetData(XML_DOM)
    XML_DOM.save('settings/files/employees.xml')

    fill_employee_list()
    return redirect('settings')


def delete_employee(request, employee_id):
    Employees.objects.get(id=employee_id).delete()
    return redirect('settings')