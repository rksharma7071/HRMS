# Generated by Django 5.0 on 2023-12-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_employee_attendance_emp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_details',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Employee'),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='lastName',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='middleName',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_details',
            name='sex',
            field=models.CharField(choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female')], default='', max_length=10),
        ),
    ]
