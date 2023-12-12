from django.db import models


class Patterns(models.Model):
    name = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


class Patterns_Devices(models.Model):
    pattern_name = models.ForeignKey('Patterns', on_delete=models.CASCADE)
    device_id = models.ForeignKey('settings.Devices', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.device_id)

    class Meta:
        verbose_name = 'Шаблон-Устройство'
        verbose_name_plural = 'Шаблон-Устройства'


class Patterns_Employees(models.Model):
    pattern_name = models.ForeignKey('Patterns', on_delete=models.CASCADE)
    employee_id = models.ForeignKey('settings.Employees', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.employee_id)

    class Meta:
        verbose_name = 'Шаблон-Сотрудник'
        verbose_name_plural = 'Шаблон-Сотрудники'


class Periods(models.Model):
    time_from = models.TimeField()
    time_to = models.TimeField()

    def __str__(self):
        return f'{self.time_from}-{self.time_to}'

    class Meta:
        verbose_name = 'Временной промежуток'
        verbose_name_plural = 'Временные промежутки'


class Absenses(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Причина пропуска'
        verbose_name_plural = 'Причины пропусков'