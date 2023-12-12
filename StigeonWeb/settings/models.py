from django.db import models


class PercoConnect(models.Model):
    host = models.CharField(unique=True)
    port = models.CharField(unique=True)
    login = models.CharField(unique=True)
    password = models.CharField(unique=True)
    sdk_name = models.CharField(unique=True)

    def __str__(self):
        return self.host

    class Meta:
        verbose_name = 'Настройки подключения'
        verbose_name_plural = 'Настройки подключения'


class Devices(models.Model):
    name = models.CharField()
    host = models.CharField()
    gateway = models.CharField()
    netmask = models.CharField()
    mac = models.CharField()
    id_internal = models.CharField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Employees(models.Model):
    last_name = models.CharField()
    first_name = models.CharField()
    middle_name = models.CharField()
    id_internal = models.CharField(unique=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Colors(models.Model):
    absenteeism = models.CharField()
    lateness = models.CharField()
    early = models.CharField()
    lateness_early = models.CharField()
    purpose = models.CharField()

    def __str__(self):
        return 'Цвета'

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'