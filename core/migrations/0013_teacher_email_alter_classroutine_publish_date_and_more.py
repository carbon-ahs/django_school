# Generated by Django 4.0 on 2023-12-22 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_classroutine_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='classroutine',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 22, 16, 33, 28, 833036)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 22, 16, 33, 28, 833036)),
        ),
    ]
