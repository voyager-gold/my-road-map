# Generated by Django 2.0.5 on 2018-12-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20181204_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='private_labeled',
            field=models.BooleanField(default=False),
        ),
    ]
