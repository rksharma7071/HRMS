# Generated by Django 5.0 on 2023-12-26 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_employee_details_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_details',
            name='img',
        ),
    ]
