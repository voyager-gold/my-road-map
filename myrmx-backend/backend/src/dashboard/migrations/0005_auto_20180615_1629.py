# Generated by Django 2.0.5 on 2018-06-15 22:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180613_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='competency',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actionitemglobal',
            name='cohort',
            field=models.ManyToManyField(blank=True, help_text='Select specific Groups that this Action Item applies to. Or leave blank if it should apply to all Cohorts, including any future Cohorts.', to='dashboard.Cohort'),
        ),
    ]
