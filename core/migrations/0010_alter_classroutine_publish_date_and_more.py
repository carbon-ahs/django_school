# Generated by Django 4.0 on 2023-12-22 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_school_email_school_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroutine',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 22, 15, 24, 29, 556533)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 22, 15, 24, 29, 548490)),
        ),
    ]