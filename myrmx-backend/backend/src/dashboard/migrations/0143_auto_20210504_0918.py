# Generated by Django 2.2.15 on 2021-05-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0142_auto_20210408_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            # PK = 1 corresponds to MyRoadmap company in all environments
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company'),
            preserve_default=False,
        ),
    ]
