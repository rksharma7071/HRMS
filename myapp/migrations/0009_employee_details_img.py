# Generated by Django 5.0 on 2023-12-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_employee_details_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_details',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='employee/'),
        ),
    ]
