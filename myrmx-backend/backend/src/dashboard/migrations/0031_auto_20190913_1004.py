# Generated by Django 2.0.5 on 2019-09-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_stage_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competency',
            name='description',
            field=models.TextField(blank=True, help_text="This is the 'Question?' that's used in the Stage overview", max_length=2048),
        ),
    ]