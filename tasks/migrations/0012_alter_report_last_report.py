# Generated by Django 4.0.1 on 2022-02-22 20:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_report_delete_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='last_report',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 22, 0, 55, 41, 545395, tzinfo=utc), null=True),
        ),
    ]