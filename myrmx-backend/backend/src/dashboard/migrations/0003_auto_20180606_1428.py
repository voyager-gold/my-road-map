# Generated by Django 2.0.5 on 2018-06-06 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_add_comment_student_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionitemglobal',
            name='due_date',
            field=models.DateField(default=datetime.date(2018, 6, 13)),
        ),
        migrations.AlterField(
            model_name='competency',
            name='description',
            field=models.CharField(blank=True, help_text="This is the 'Question?' that's used in the Stage overview", max_length=255),
        ),
        migrations.AlterField(
            model_name='competency',
            name='green_description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='competency',
            name='red_description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='competency',
            name='yellow_description',
            field=models.CharField(max_length=255),
        ),
    ]
