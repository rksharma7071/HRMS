# Generated by Django 5.0 on 2023-12-26 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_employee_details_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='employee')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee_details')),
            ],
        ),
    ]
