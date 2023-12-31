# Generated by Django 4.2.2 on 2023-07-04 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_employees'),
        ('patterns', '0002_patterns_devices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patterns_Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.employees')),
                ('pattern_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patterns.patterns')),
            ],
            options={
                'verbose_name': 'Шаблон-Устройство',
                'verbose_name_plural': 'Шаблон-Устройства',
            },
        ),
    ]
