# Generated by Django 2.0.5 on 2019-10-05 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20191003_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='coach_synonym',
            field=models.CharField(blank=True, default='Coach', max_length=50, null=True),
        ),
    ]
