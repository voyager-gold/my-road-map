# Generated by Django 2.0.5 on 2020-02-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0097_auto_20200204_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='competency',
            name='daily_assessment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='NFfWvZ3tRXZg1TpOk0kww7J5ISSh9TeCaswAd2Sz7w0injGDQ6EGAqO8DRZE5OpUcC5lWGaXSWN'),
        ),
    ]
