# Generated by Django 5.0 on 2023-12-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_employee_details_img_alter_employee_details_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/employee/'),
        ),
    ]